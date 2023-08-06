from django.db import models
from django.contrib.auth.models import User

import uuid

from dotenv import load_dotenv
import os
import secrets
import string


class Profile(models.Model):
  GENDER_CHOICES = (
      ('M', "ذكر"),
      ('F', "أنثي")
  )
  DEACONESS_CHOICES = (
      ('غير', "غير مرشوم"),
      ('أغس', "أغنسطس"),
      ('إبس', "إبسالطس")
  )

  DEFAULT_PROFILE_PATH = 'images/profiles/user-default.png'

  user = models.OneToOneField(
      User, on_delete=models.CASCADE, null=True, blank=False)
  name = models.CharField(max_length=200, unique=True)
  birthdate = models.DateField(null=True, blank=False)
  talmza_level = models.ForeignKey(
      "TalmzaLevel", on_delete=models.SET_NULL, null=True, blank=False)
  current_talmza_level_year = models.IntegerField(
      default=1, null=True, blank=False)
  school_level = models.ForeignKey(
      "SchoolLevel", on_delete=models.SET_NULL, null=True, blank=False)
  current_school_level_year = models.IntegerField(
      default=1, null=True, blank=True)
  address = models.OneToOneField(
      "Address", on_delete=models.SET_NULL, null=True, blank=True)
  job = models.CharField(max_length=200, null=True, blank=True)
  gender = models.CharField(
      max_length=1, choices=GENDER_CHOICES, default=GENDER_CHOICES[0])
  phone_number = models.CharField(max_length=11, null=True, blank=True)
  father_phone_number = models.CharField(max_length=11, null=True, blank=True)
  mother_phone_number = models.CharField(max_length=11, null=True, blank=True)
  mobile_follow_up_on_WhatsApp = models.CharField(
      max_length=11, null=True, blank=True)
  confession_father = models.CharField(max_length=200, null=True, blank=True)
  church = models.CharField(
      max_length=200, default="كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال")
  deaconess = models.CharField(max_length=10, choices=DEACONESS_CHOICES)
  profile_image = models.ImageField(
      null=True, blank=True, upload_to='images/profiles', default=DEFAULT_PROFILE_PATH)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return str(self.name + " " + self.user.username)
    # return str(self.name)

  def levelUpTalmza(self):
    maxYear = self.talmza_level.number_of_years
    currentYear = self.current_talmza_level_year

    if self.talmza_level.next_level or currentYear < maxYear:
      if currentYear == maxYear:
        self.talmza_level = self.talmza_level.next_level
        self.current_talmza_level_year = 1
      else:
        self.current_talmza_level_year += 1

      self.save()
      return True
    else:
      return False

  def levelDownTalmza(self):
    maxYear = self.talmza_level.number_of_years
    currentYear = self.current_talmza_level_year

    if self.talmza_level.prevues_level or currentYear > 1:
      if currentYear == 1:
        self.talmza_level = self.talmza_level.prevues_level
        self.current_talmza_level_year = self.talmza_level.number_of_years
      else:
        self.current_talmza_level_year -= 1

      self.save()
      return True
    else:
      return False

  def levelUpSchool(self):
    maxYear = self.school_level.number_of_years
    currentYear = self.current_school_level_year

    if self.school_level.level_number in [0, 5, 6]:
      return False

    if self.school_level.next_level or currentYear < maxYear:
      if currentYear == maxYear:
        self.school_level = self.school_level.next_level
        self.current_school_level_year = 1
      else:
        self.current_school_level_year += 1

      self.save()
      return True
    else:
      return False

  def levelDownSchool(self):
    maxYear = self.school_level.number_of_years
    currentYear = self.current_school_level_year

    if self.school_level.level_number in [0, 5, 6]:
      return False

    if self.school_level.prevues_level:
      if currentYear == 1:
        self.school_level = self.school_level.prevues_level
        self.current_school_level_year = 2
      else:
        self.current_school_level_year -= 1

      self.save()
      return True
    else:
      return False

  def generatePassword(length=6):
    alphabet = string.digits  # + string.ascii_letters + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

  def getProfileName(request, context):
    profile = Profile.objects.get(user__id=request.user.id)
    context['profileName'] = profile.name


class Address(models.Model):
  building = models.CharField(max_length=50, null=True, blank=True)
  street = models.CharField(max_length=50, null=True, blank=True)
  branches_from = models.CharField(max_length=50, null=True, blank=True)
  floor = models.CharField(max_length=50, null=True, blank=True)
  apartment_number = models.CharField(max_length=50, null=True, blank=True)
  residential_complexes = models.CharField(
      max_length=50, null=True, blank=True)
  district = models.CharField(max_length=50, null=True, blank=True)
  additional_details = models.TextField(max_length=500, null=True, blank=True)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    details = []
    if self.building:
      details.append(f"مبنا: {self.building}")
    if self.street:
      details.append(f"شارع: {self.street}")
    if self.branches_from:
      details.append(f"متفرع من: {self.branches_from}")
    if self.floor:
      details.append(f"الطابق: {self.floor}")
    if self.apartment_number:
      details.append(f"رقم الشقة: {self.apartment_number}")
    if self.residential_complexes:
      details.append(f"مجمع سكني: {self.residential_complexes}")
    if self.district:
      details.append(f"الحي: {self.district}")
    if self.additional_details:
      details.append(f"تفاصيل إضافية: {self.additional_details}")

    return ', '.join(details)

  def getAddressFromRequset(request, oldAddress=None):

    building = request.POST.get("building")
    street = request.POST.get("street")
    branches_from = request.POST.get("branches_from")
    floor = request.POST.get("floor")
    apartment_number = request.POST.get("apartment_number")
    residential_complexes = request.POST.get("residential_complexes")
    district = request.POST.get("district")
    additional_details = request.POST.get("additional_details")

    if oldAddress:
      oldAddress.building = building
      oldAddress.street = street
      oldAddress.branches_from = branches_from
      oldAddress.floor = floor
      oldAddress.apartment_number = apartment_number
      oldAddress.residential_complexes = residential_complexes
      oldAddress.district = district
      oldAddress.additional_details = additional_details

      oldAddress.save()
      return oldAddress
    else:
      address = Address.objects.create(
          building=building,
          street=street,
          branches_from=branches_from,
          floor=floor,
          apartment_number=apartment_number,
          residential_complexes=residential_complexes,
          district=district,
          additional_details=additional_details
      )
      return address

  def getAddressAttributesInContext(self, context):

    context['building'] = self.building
    context['street'] = self.street
    context['branches_from'] = self.branches_from
    context['floor'] = self.floor
    context['apartment_number'] = self.apartment_number
    context['residential_complexes'] = self.residential_complexes
    context['district'] = self.district
    context['additional_details'] = self.additional_details


class TalmzaLevel(models.Model):
  level_name = models.CharField(max_length=50)
  level_number = models.IntegerField()
  number_of_years = models.IntegerField(default=2)
  next_level = models.OneToOneField(
      "TalmzaLevel", related_name="talmza_next_level", on_delete=models.SET_NULL, null=True, blank=True)
  prevues_level = models.OneToOneField(
      "TalmzaLevel", related_name="talmza_prevues_level", on_delete=models.SET_NULL, null=True, blank=True)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  class Meta:
    ordering = ['level_number']

  def __str__(self):
    return str(self.level_name)


class SchoolLevel(models.Model):
  level_name = models.CharField(max_length=50)
  level_number = models.IntegerField()
  number_of_years = models.IntegerField(null=True, blank=True)
  next_level = models.OneToOneField(
      "SchoolLevel", related_name="school_next_level", on_delete=models.SET_NULL, null=True, blank=True)
  prevues_level = models.OneToOneField(
      "SchoolLevel", related_name="school_prevues_level", on_delete=models.SET_NULL, null=True, blank=True)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  class Meta:
    ordering = ['level_number']

  def __str__(self):
    return str(self.level_name)


class ExpensesProfileForm(models.Model):
  year = models.CharField(max_length=4)
  amount_of_money_payed = models.IntegerField()
  created_for = models.ForeignKey(
      Profile, on_delete=models.SET_NULL, null=True, blank=False)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return self.year + " " + str(str(self.created_for) + " دفع " + str(self.amount_of_money_payed) + " جنيهات")

  # total number of Expenses (not as a proprty in the table but an constant stored in a spearte table or as .env file in backend)
  def getExpenses() -> int:
    load_dotenv()
    return int(os.getenv("EXPENSES_PROFILE_FORM"))

  # -------------------------------- validation -------------------------------- #
  def validateAmountPayed(amount):
    expenses = ExpensesProfileForm.getExpenses()
    if amount == '':
      return False

    if amount.isdigit():
      amount = int(amount)
    else:
      return False

    if amount < 1 or amount > expenses:
      return False

    return True


class ProfileFormLog(models.Model):
  CATEGORY_ACTION_CHOICES = (
      ('D', "Delete"),
      ('A', "ADD"),
      ('E', "Edit")
  )
  created_for = models.ForeignKey(
      Profile, related_name="created_for", on_delete=models.SET_NULL, null=True, blank=False)
  log_date = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(
      Profile, related_name="created_by", on_delete=models.SET_NULL, null=True, blank=False)
  category_action = models.CharField(
      max_length=1, choices=CATEGORY_ACTION_CHOICES)
  action = models.TextField(max_length=2000)
  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return str(self.created_for + " دفع " + str(self.amount_of_money_payed) + "جنيهات")
