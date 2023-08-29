import datetime
import json
from datetime import date, timedelta
from pathlib import Path

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from users import models
from users.forms import ProfileForm

currentYear = datetime.date.today().year


@ login_required(login_url='sign-in')
def profileForm(request):
  if ((request.method == 'GET' and request.GET.get('id')) or (request.method == 'POST' and request.POST.get('userId'))):
    return updateProfileForm(request)
  else:
    return newProfileForm(request)


def putBirthdateFieldInContext(profile, context):
  birthdate = None
  if profile:
    birthdate = profile.birthdate

  context["birthdate"] = birthdate


def putTalmzaFieldInContext(profile, context):
  talmzaLevels = models.TalmzaLevel.objects.filter()

  talmzaChoices = []

  for level in talmzaLevels:
    isSelected = False
    if profile:
      isSelected = profile.talmza_level.id == level.id
    talmzaChoices.append((level.id, level.level_name, isSelected))

  context["talmzaChoices"] = talmzaChoices


def putSchoolFieldInContext(profile, context):
  schoolLevels = models.SchoolLevel.objects.filter()

  schoolChoices = []

  for level in schoolLevels:
    isSelected = False
    if profile:
      isSelected = profile.school_level.id == level.id
    schoolChoices.append((level.id, level.level_name, isSelected))

  context["schoolChoices"] = schoolChoices


@login_required(login_url='sign-in')
def newProfileForm(request):
  context = {}
  profile = None
  profileForm = ProfileForm()

  if request.method == 'POST':

    profileForm = ProfileForm(
        request.POST, request.FILES)

    if profileForm.is_valid():
      amount_of_money_payed = getAmountOfMoneyPayed(request)
      profile = profileForm.save(commit=False)

      if models.ExpensesProfileForm.validateAmountPayed(amount_of_money_payed):
        profile.address = models.Address.getAddressFromRequset(request)
        profile.user = createNewUser(context)

        profile.save()
        addDefaultTagToNewProfile(profile)

        createNewExpenses(amount_of_money_payed, profile, context)
      else:
        context["showModal"] = True
        context["expensesError"] = "أدخل المصاريف بشكل صحيح."

  path = Path(request.path)

  context['expenses'] = models.ExpensesProfileForm.getExpenses()
  context['profileForm'] = profileForm
  context['pageName'] = path.name

  models.Profile.getProfileName(request, context)
  putSchoolFieldInContext(profile, context)
  putTalmzaFieldInContext(profile, context)
  putBirthdateFieldInContext(profile, context)
  return render(request, 'users/profileForm.html', context)


@ login_required(login_url='sign-in')
def updateProfileForm(request):
  context = {}
  profile = None
  profileForm = ProfileForm()

  if request.method == 'GET':
    profileIdSearch = request.GET.get('id')

    profile = getProfileIfExists(context, profileIdSearch)
    profileForm = ProfileForm(instance=profile)

  if request.method == 'POST':
    profileIdSearch = request.POST['userId']
    profile = getProfileIfExists(context, profileIdSearch)
    profileForm = ProfileForm(
        request.POST, request.FILES, instance=profile)

    if profileForm.is_valid():
      amount_of_money_payed = getAmountOfMoneyPayed(request)
      profile = profileForm.save(commit=False)

      if models.ExpensesProfileForm.validateAmountPayed(amount_of_money_payed):
        updateProfileAddress(profile, request)
        profile.save()
        try:
          expenses = models.ExpensesProfileForm.objects.get(
              year=str(currentYear), created_for=profile)
        except:
          expenses = None

        if expenses:
          updateOldExpenses(amount_of_money_payed, expenses, context)
        else:
          createNewExpenses(amount_of_money_payed, profile, context)
      else:
        context["showModal"] = True
        context["expensesError"] = "أدخل المصاريف بشكل صحيح."

  if profile:
    try:
      expensesPayed = models.ExpensesProfileForm.objects.get(
          created_for__id=profile.id, year=currentYear)
      context["expensesPayed"] = expensesPayed.amount_of_money_payed
    except:
      context["expensesPayedMessage"] = "لا يوجد مبلغ مدفوع من قبل."
      context["expensesPayed"] = 0
    context["names"] = profile.name.split(" ")
    profile.address.getAddressAttributesInContext(context)
  context["userId"] = profileIdSearch

  path = Path(request.path)

  context['expenses'] = models.ExpensesProfileForm.getExpenses()
  context['profileForm'] = profileForm
  context['pageName'] = path.name

  models.Profile.getProfileName(request, context)
  putSchoolFieldInContext(profile, context)
  putTalmzaFieldInContext(profile, context)
  putBirthdateFieldInContext(profile, context)
  return render(request, 'users/profileForm.html', context)


def getProfileIfExists(context, id):
  try:
    return models.Profile.objects.get(user__username=id)
  except:
    context["errorProfileNotFound"] = "رقم التسجيل غير صحيح"
    return None


def getAmountOfMoneyPayed(request):
  return request.POST.get('amount_of_money_payed', '')


def updateProfileAddress(profile, request):
  if profile.address:
    profile.address = models.Address.getAddressFromRequset(
        request, profile.address)
  else:
    profile.address = models.Address.getAddressFromRequset(request)


def createNewExpenses(amount_of_money_payed, profile, context):
  newExpenses = models.ExpensesProfileForm.objects.create(
      year=str(currentYear),
      amount_of_money_payed=amount_of_money_payed,
      created_for=profile
  )
  context["expensesPayedReadOnly"] = True
  context["expensesPayed"] = newExpenses.amount_of_money_payed
  # TODO log line


def updateOldExpenses(newMoneyPayed, expenses, context):
  if int(newMoneyPayed) >= expenses.amount_of_money_payed:
    expenses.amount_of_money_payed = newMoneyPayed
    expenses.save()
    context["expensesPayedReadOnly"] = True
    context["expensesPayed"] = expenses.amount_of_money_payed

    # TODO log line
  else:
    context["showModal"] = True
    context["expensesError"] = "المبلغ المدخل اقل من المسجل في الموقع."


def createNewUser(context):
  generatedPassword = models.Profile.generatePassword()
  hashedPassord = make_password(generatedPassword)
  user = User.objects.create(username="", password=hashedPassord)
  context["showModal"] = True
  context["profilePassword"] = generatedPassword
  context["profileId"] = user.username
  return user


def addDefaultTagToNewProfile(profile):
  defaultTag = models.UserPermissionTag.objects.get(is_buttom=True)
  profile.user_permission_tags.add(defaultTag)
