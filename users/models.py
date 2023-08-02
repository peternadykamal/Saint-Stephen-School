from argparse import Action
from ast import mod, pattern
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

import uuid

from dotenv import load_dotenv
import os


class Profile(models.Model):
  GENDER_CHOICES = (
      ('M', "مذكر"),
      ('F', "مؤنث")
  )
  DEACONESS_CHOICES = (
      ('غير', "غير مرشوم"),
      ('أغس', "أغنسطس"),
      ('إبس', "إبسالطس")
  )

  user = models.OneToOneField(
      User, on_delete=models.CASCADE)
  # user = models.OneToOneField(
  #   User, on_delete=models.CASCADE, null=True, blank=False)
  name = models.CharField(max_length=200, unique=True)
  birthdate = models.DateField(null=True, blank=False)
  talmza_level = models.ForeignKey(
      "TalmzaLevel", on_delete=models.SET_NULL, null=True, blank=True)
  current_talmza_level_year = models.IntegerField(default=1)
  school_level = models.ForeignKey(
      "SchoolLevel", on_delete=models.SET_NULL, null=True, blank=True)
  current_school_level_year = models.IntegerField(default=1)
  address = models.OneToOneField(
      "Address", on_delete=models.SET_NULL, null=True, blank=True)
  job = models.CharField(max_length=200, null=True, blank=True)
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
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
      null=True, blank=True, upload_to='images/profiles', default='images/profiles/user-default.png')

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return str(self.name + " " + self.user.username)

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
    return str(" المستوي " + self.level_name)


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
    return str(" الصف " + self.level_name)


class ExpensesProfileForm(models.Model):
  year = models.CharField(max_length=4)
  amount_of_money_payed = models.IntegerField()
  created_for = models.ForeignKey(
      Profile, on_delete=models.SET_NULL, null=True, blank=False)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return str(self.created_for + " دفع " + str(self.amount_of_money_payed) + "جنيهات")

  # total number of Expenses (not as a proprty in the table but an constant stored in a spearte table or as .env file in backend)
  def getExpenses() -> int:
    load_dotenv()
    return int(os.getenv("EXPENSES_PROFILE_FORM"))


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