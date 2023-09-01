from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from users import models

# this middle ware is use to add the user profile to the request if the user is logged in


class UserProfileMiddleware(MiddlewareMixin):
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
      try:
        # Fetch the user's profile
        request.profile = models.Profile.objects.get(user=request.user)
      except models.Profile.DoesNotExist:
        # Handle the case where a profile doesn't exist
        request.profile = None
        logout(request)
        return redirect('landing')

    response = self.get_response(request)
    return response
