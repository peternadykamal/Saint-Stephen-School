from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.http import (require_GET, require_http_methods,
                                          require_POST)

from decorators.checkPermissionDecorator import check_permission_level
from users import models
from users.models.UserPermissionTagModel import UserPermissionTag


@login_required(login_url='sign-in')
@require_GET
def searchUsers(request):
  query = request.GET.get('q', '')
  age_filter = request.GET.get('age', None)
  gender_filter = request.GET.get('gender', None)
  highest_tag_filter = request.GET.get('highest_tag', None)

  users = models.Profile.objects.filter(Q(name__icontains=query)).with_age()

  if age_filter:
    # Assuming 'age_filter' is in the format 'min_age-max_age'
    min_age, max_age = map(int, age_filter.split('-'))
    # make sure min_age <= max_age
    if min_age > max_age:
      min_age, max_age = max_age, min_age

    # users = [user for user in users if min_age <= user.age <= max_age]
    users = users.filter(age__range=(min_age, max_age))

  if gender_filter:
    # check gender_filter is valid
    gender_values = [choice[0]
                     for choice in models.Profile.GENDER_CHOICES]
    if gender_filter in gender_values:
      users = users.filter(gender=gender_filter)

  # Filter users based on the highest tag
  if highest_tag_filter:
    highest_tag_filter_obj = UserPermissionTag.objects.filter(
        tag_name=highest_tag_filter).first()
    if highest_tag_filter_obj:
      users = users.filter(highest_tag=highest_tag_filter_obj)

  # filter users based on if there highest tag is lower than the user's highest tag
  highest_tag_logged_in_user = request.profile.highest_tag
  if highest_tag_logged_in_user:
    users = users.filter(
        highest_tag__order__gt=highest_tag_logged_in_user.order)

  user_list = list(users.values('age', 'highest_tag__tag_name',
                   'name', 'user__username', 'gender', 'profile_image', 'id'))
  # user_list = list(users.values())

  # filter user_list to contain only age, highest_tag, name, user.username, gender

  # Pagination
  page = request.GET.get('page', 1)
  paginator = Paginator(user_list, 10)  # 10 users per page
  try:
    users_page = paginator.page(page)
  except PageNotAnInteger:
    users_page = paginator.page(1)
  except EmptyPage:
    users_page = paginator.page(paginator.num_pages)

  response_data = {
      'users': list(users_page),
      'query': query,
      'total_pages': paginator.num_pages,
      'current_page': users_page.number,
  }
  return JsonResponse(response_data)
  # Convert the QuerySet to a list of dictionaries
  # user_list = list(users.values())
  # return JsonResponse({'users': user_list, 'query': query})


@require_GET
@check_permission_level()
def getUserProfile(request, user_id):
  target_user = models.Profile.objects.filter(id=user_id).first()
  user_profile = target_user.to_dict()
  return JsonResponse({'user': user_profile})

# @require_POST
# def changePassword():
