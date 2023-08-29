from django.http import HttpResponse
from django.http import HttpResponseForbidden
from users.models import Profile
from django.conf import settings
import os


def mediaAccess(request, path):
  access_granted = False
  user = request.user
  if user.is_authenticated:
    if user.is_staff:
      # If admin, everything is granted
      access_granted = True
    else:
      profile = Profile.getProfileByUserName(user)
      if profile:
        # For simple user, only their documents can be accessed
        user_documents = [
            profile.profile_image.name,
            Profile.DEFAULT_PROFILE_PATH,
            # add here more allowed documents
        ]
        for doc in user_documents:
          if path == doc:
            access_granted = True

  if access_granted:
    response = HttpResponse()
    # TODO make protected get loaded from .env file or from settings file
    response['X-Accel-Redirect'] = f'/protected/{path}'
    # Content-type will be detected by nginx
    del response['Content-Type']
    return response
  else:
    return HttpResponseForbidden('Not authorized to access this media.')
