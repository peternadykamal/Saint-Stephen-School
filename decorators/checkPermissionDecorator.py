# library_app/decorators.py

from functools import wraps
import profile
from django.http import Http404
from users.models import UserPermissionTag, Profile


def has_permission_tag(tag_name):
  def decorator(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
      user = request.user
      try:
        profile = Profile.objects.get(user__username=user.username)
        tag = UserPermissionTag.objects.get(tag_name=tag_name)
        if profile.user_permission_tags.filter(name=tag.tag_name).exists():
          return view_func(request, *args, **kwargs)
        else:
          raise Http404("Page not found")
      except UserPermissionTag.DoesNotExist:
        raise Http404("Page not found")
    return _wrapped_view
  return decorator
