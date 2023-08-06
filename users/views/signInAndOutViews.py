from math import exp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from users import models
from users.forms import ProfileForm

import datetime
from datetime import timedelta, date
from pathlib import Path
import json


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
