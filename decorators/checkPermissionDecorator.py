# library_app/decorators.py

import profile
from functools import wraps
from math import perm
from typing import Callable

from django.http import Http404

from users.models import Profile, UserPermissionTag
from users.models.PermissionLogModel import PermissionLog


def has_permission_tag(tag_name):
  def decorator(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
      user = request.user
      try:
        profile = Profile.objects.get(user__username=user.username)
        tag = UserPermissionTag.objects.get(tag_name=tag_name)
        if profile.user_permission_tags.filter(tag_name=tag.tag_name).exists():
          return view_func(request, *args, **kwargs)
        else:
          raise Http404("Page not found")
      except UserPermissionTag.DoesNotExist:
        raise Http404("Page not found")
    return _wrapped_view
  return decorator


def has_permission(permission_codename):
  def decorator(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
      try:
        PermissionLog.objects.create(
            user=request.user, permission_codename=permission_codename)
        permissions = request.profile.getAllPermissions()
        permissionsCodename = [item.codename for item in permissions]
        if permission_codename in permissionsCodename:
          return view_func(request, *args, **kwargs)
        else:
          raise Http404("Page not found")
      except UserPermissionTag.DoesNotExist:
        raise Http404("Page not found")
    return _wrapped_view
  return decorator


def check_permission_level(permission_check: Callable[[Profile, Profile], bool] =
                           lambda requesting_user, target_user: target_user.highest_tag.order > requesting_user.highest_tag.order):
  ''' 
  this decorator used if the requesting user have the right to do the action on the target user \n
  permission_check is a function that takes two arguments (requesting_user, target_user) and 
  returns True if the requesting_user have the right to do the action on the target_user

  ### Example:
  ```python
  def permission_check(requesting_user, target_user):
    return target_user.highest_tag.order > requesting_user.highest_tag.order

  @check_permission_level(permission_check)
  def view_func(request, *args, **kwargs):
  ```
  Note: if permission_check have a defualt value, which is checking if the target_user's highest_tag.order is greater than the requesting_user's highest_tag.order
  '''
  def decorator(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
      # Get the target user and requesting user from the request or kwargs
      target_user_id = kwargs.get('user_id', None)
      requesting_user = request.profile

      # if target_user is None
      if not target_user_id:
        raise Http404("Page not found")

      target_user = Profile.objects.filter(id=target_user_id).first()

      # if target_user is None
      if not target_user:
        raise Http404("Page not found")

      # if target_user.highest_tag.order > requesting_user.highest_tag.order:
      #   return view_func(request, *args, **kwargs)

      if permission_check and not permission_check(requesting_user, target_user):
        raise Http404("Page not found")

      return view_func(request, *args, **kwargs)

    return _wrapped_view

  return decorator
