from django.db import models
from django.contrib.auth.models import User

import uuid

import secrets
import string

from .addressModel import Address
from .talmzaLevelModel import TalmzaLevel
from .schoolLevelModel import SchoolLevel
from .UserPermissionTagModel import UserPermissionTag


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
      TalmzaLevel, on_delete=models.SET_NULL, null=True, blank=True)
  current_talmza_level_year = models.IntegerField(
      default=1, null=True, blank=True)
  school_level = models.ForeignKey(
      SchoolLevel, on_delete=models.SET_NULL, null=True, blank=False)
  current_school_level_year = models.IntegerField(
      default=1, null=True, blank=True)
  address = models.OneToOneField(
      Address, on_delete=models.SET_NULL, null=True, blank=True)
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
  user_permission_tags = models.ManyToManyField(
      UserPermissionTag, blank=True)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    # return str(self.name + " " + self.user.username)
    return str(self.name)

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

    if self.talmza_level.previous_level or currentYear > 1:
      if currentYear == 1:
        self.talmza_level = self.talmza_level.previous_level
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

    if self.school_level.previous_level:
      if currentYear == 1:
        self.school_level = self.school_level.previous_level
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
