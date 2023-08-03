from math import exp
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

import datetime
from datetime import timedelta, date
from pathlib import Path
import json


@ login_required(login_url='sign-in')
def profileForm(request):
  context = {}
  profileForm = ProfileForm()

  contentType = request.META.get('CONTENT_TYPE')
  if request.method == 'POST':
    year = datetime.date.today().year
    if contentType == 'multipart/form-data':
      profileForm = ProfileForm(request.POST, request.FILES)
      if profileForm.is_valid():
        profile = profileForm.save(commit=False)

        # TODO still want to test it
        if profile.address:
          profile.address = models.Address.getAddressFromRequset(
              request, profile.address)
        else:
          profile.address = models.Address.getAddressFromRequset(request)

        amount_of_money_payed = request.POST.get('amount_of_money_payed')

        if models.ExpensesProfileForm.validateAmountPayed(amount_of_money_payed):

          if not profile.user:
            generatedPassword = models.Profile.generatePassword()
            hashedPassord = make_password(generatedPassword)
            user = User.objects.create(username="", password=hashedPassord)
            profile.user = user
            context["showModal"] = True
            context["profilePassword"] = generatedPassword
            context["profileId"] = user.username

          profile.save()

          try:
            expenses = models.ExpensesProfileForm.objects.get(
                year=str(year), created_for=profile)
          except:
            expenses = None

          if expenses:
            if amount_of_money_payed >= expenses.amount_of_money_payed:
              expenses.amount_of_money_payed = amount_of_money_payed
              expenses.save()
              context["expensesPayedReadOnly"] = True
              context["expensesPayed"] = expenses.amount_of_money_payed

              # TODO log line
            else:
              context["showModal"] = True
              context["expensesError"] = "المبلغ المدخل اقل من المسجل في الموقع."
          else:
            newExpenses = models.ExpensesProfileForm.objects.create(
                year=str(year),
                amount_of_money_payed=amount_of_money_payed,
                created_for=profile
            )
            context["expensesPayedReadOnly"] = True
            context["expensesPayed"] = newExpenses.amount_of_money_payed
            # TODO log line
        else:
          context["showModal"] = True
          context["expensesError"] = "أدخل المصاريف بشكل صحيح."
    elif contentType == 'application/json':
      data = json.loads(request.body)
      profileIdSearch = data.get('profileIdSearch')
      # print(profileIdSearch)
      try:
        profile = models.Profile.objects.get(user__username=profileIdSearch)
        profileForm = ProfileForm(instance=profile)
        oldExpenses = models.ExpensesProfileForm.objects.get(
            created_for__id=profile.id, year=year)
        print(profile)
        context["expensesPayed"] = oldExpenses.amount_of_money_payed
      except:
        context["errorProfileNotFound"] = "رقم التسجيل غير صحيح"

  path = Path(request.path)

  context['expenses'] = models.ExpensesProfileForm.getExpenses()
  context['profileForm'] = profileForm
  context['pageName'] = path.name

  models.Profile.getProfileName(request, context)
  rendered_html = render(request, 'users/profileForm.html', context)
  if contentType == 'application/json':
    return HttpResponse(rendered_html.content, content_type='text/html')
  else:
    return rendered_html


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
