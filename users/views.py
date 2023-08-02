from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from . import models
from .forms import ProfileForm

from datetime import timedelta, date
from pathlib import Path
import json


@ login_required(login_url='sign-in')
def profileForm(request):
  profileForm = ProfileForm()
  if request.method == 'POST':
    profileForm = ProfileForm(request.POST, request.FILES)
    if profileForm.is_valid():
      profile = profileForm.save(commit=False)

      generatedPassword = models.Profile.generatePassword()
      hashedPassord = make_password(generatedPassword)
      user = User.objects.create(username="", password=hashedPassord)

      profile.address = models.Address.getAddressFromRequset(request)
      profile.user = user

      profile.save()
      # return HttpResponse("استمارة تمت بنجاح!")
    # else:
      # return HttpResponse("حدث خطأ أثناء التسجيل.")

  path = Path(request.path)

  context = {'profileForm': profileForm,
             'pageName': path.name,
             }
  models.Profile.getProfileName(request, context)
  return render(request, 'users/profileForm.html', context)


def signIn(request):
  if request.user.is_authenticated:
    return redirect('landing')
  context = {}
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    try:
      remember_me = request.POST['remember-me'] == 'remember'
    except:
      remember_me = False

    # it will return back either the user instance or it's going to return none
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      if not remember_me:
        # Calculate the number of seconds in 30 days
        expirationTime = timedelta(days=30).total_seconds()
        request.session.set_expiry(expirationTime)
      return redirect('landing')
    else:
      # one of them
      # messages.error(request, "Username OR password is incorrect")
      # return HttpResponse("Username OR password is incorrect")
      context['errorSignInMessage'] = "رقم المستخدم أو كلمة المرور غير صحيحة"

  return render(request, 'users/signIn.html', context)


def logoutUser(request):
  logout(request)
  return redirect('landing')


def getSchoolLevelYears(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      data = json.loads(request.body)
      selectedSchoolLevel = data.get('school_level_id')

      schoolLevel = models.SchoolLevel.objects.get(
          id=selectedSchoolLevel)

      levelYears = schoolLevel.number_of_years

      show = ""
      years = []

      match schoolLevel.level_number:
        case 0:
          show = "Null"
        case 5 | 6:
          show = "textField"
        case _:
          show = "dropBox"
          years = list(range(1, levelYears + 1))

      data = {
          'getSchoolLevelYears': years,
          'show': show
      }
    return JsonResponse(data, safe=False)


def getTalmzaLevelYears(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      data = json.loads(request.body)
      selectedSchoolLevel = data.get('talmza_level_id')

      levelYears = models.TalmzaLevel.objects.get(
          id=selectedSchoolLevel).number_of_years

    return JsonResponse(list(range(1, levelYears + 1)), safe=False)
