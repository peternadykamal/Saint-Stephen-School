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
