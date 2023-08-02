from django.shortcuts import render
from django.contrib import messages

from . import models
from .forms import ProfileForm


def testForm(request):
  profileForm = ProfileForm()
  if request.method == 'POST':
    profileForm = ProfileForm(request.POST)
    if profileForm.is_valid():
      profile = profileForm.save()
      # TODO here we want to create user and link profile with it, so we want password!
      messages.success(request, 'استمارة تمت بنجاح!')
    else:
      messages.error(
          request, 'حدث خطأ أثناء التسجيل.')
  context = {'profileForm': profileForm}
  return render(request, 'users/testForm.html', context)
