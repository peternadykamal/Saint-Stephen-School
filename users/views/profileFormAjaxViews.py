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

      if schoolLevel.level_number == 0:
        show = "Null"
      elif schoolLevel.level_number in [5, 6]:
        show = "textField"
      else:
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
