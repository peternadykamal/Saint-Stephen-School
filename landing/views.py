import profile
from django.shortcuts import render


from users import models


def landing(request):

  context = {}
  if request.user.is_authenticated:
    models.Profile.getProfileName(request, context)

  return render(request, 'landing/index.html', context)
