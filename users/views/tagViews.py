from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from decorators.checkPermissionDecorator import has_permission_tag
from users import models
from users.forms import UserPermissionTagForm


@ login_required(login_url='sign-in')
@ has_permission_tag(tag_name='admin')
def tagsPage(request):
  context = {'request': request}
  models.Profile.getProfileName(request, context)
  # add to context the tags
  tags = models.UserPermissionTag.get_sorted_tags()
  context["tags"] = tags
  return render(request, 'tags/tagsPage.html', context)
