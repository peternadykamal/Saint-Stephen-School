import profile
import secrets
import string
import uuid
from datetime import date
from operator import is_

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Case, ExpressionWrapper, IntegerField, Q, When
from django.forms import model_to_dict

from users.models.PermissionLogModel import PermissionLog

from .addressModel import Address
from .schoolLevelModel import SchoolLevel
from .talmzaLevelModel import TalmzaLevel
from .UserPermissionTagModel import UserPermissionTag


class ProfileQuerySet(models.QuerySet):
  def with_age(self) -> models.QuerySet:
    today = date.today()
    age_expression = ExpressionWrapper(
        today.year - models.F('birthdate__year') - Case(
            When(
                Q(birthdate__month__gt=today.month) |
                (Q(birthdate__month=today.month) &
                 Q(birthdate__day__gt=today.day)),
                then=1
            ),
            default=0,
            output_field=IntegerField()
        ),
        output_field=IntegerField()
    )
    return self.annotate(age=age_expression)


class ProfileManager(models.Manager):
  def get_queryset(self):
    return ProfileQuerySet(self.model, using=self._db)


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

  DEFAULT_PROFILE_PATH = 'images/user-default.png'

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
      UserPermissionTag, blank=True, related_name='profiles_with_user_permission_tag')
  highest_tag = models.ForeignKey(
      UserPermissionTag, on_delete=models.SET_NULL, null=True, blank=True, related_name='profile_with_highest_tag')

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  @property
  def age(self):
    today = date.today()
    if self.birthdate:
      age = today.year - self.birthdate.year - \
          ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
      return age
    return None

  objects = ProfileManager()

  def __str__(self):
    # return str(self.name + " " + self.user.username)
    return str(self.name)

  def to_dict(self):  # this function is used when we want to return the profile data as a json object for read only purposes
    data = model_to_dict(self, exclude=['talmza_level', 'school_level',
                         'address', 'profile_image', 'user_permission_tags', 'highest_tag'])

    data['registration_id'] = self.user.username
    data['talmza_level'] = {'level_name': self.talmza_level.level_name,
                            'id': self.talmza_level.id} if self.talmza_level else None
    data['school_level'] = {'level_name': self.school_level.level_name,
                            'id': self.school_level.id} if self.school_level else None
    data['address'] = model_to_dict(self.address) if self.address else None
    data['profile_image'] = self.profile_image.url if self.profile_image else None
    data['user_permission_tags'] = [
        {'order': item.order, 'tag_name': item.tag_name, 'id': item.id} for item in self.user_permission_tags.all()]
    data['highest_tag'] = {'order': self.highest_tag.order, 'tag_name': self.highest_tag.tag_name,
                           'id': self.highest_tag.id} if self.highest_tag else None

    return data

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

  def getHighestPermissionTag(self):
    try:
      lowestTag = UserPermissionTag.objects.get(is_buttom=True)
      currentTag = lowestTag
      profileTagsId = [item.id for item in self.user_permission_tags.all()]

      i = 0
      while (currentTag != None):
        if currentTag.id in profileTagsId:
          if (len(profileTagsId) == 1):
            return self.user_permission_tags.get(id=currentTag.id), i
          else:
            profileTagsId.remove(currentTag.id)

        currentTag = currentTag.parent
        i += 1

      return None, -1
    except:
      return None, -1

  def getLowestPermissionTag(self):
    try:
      highestTag = UserPermissionTag.objects.get(is_top=True)
      currentTag = highestTag
      profileTagsId = [item.id for item in self.user_permission_tags.all()]

      i = UserPermissionTag.objects.all().count() - 1
      while (currentTag != None):
        if currentTag.id in profileTagsId:
          if (len(profileTagsId) == 1):
            return self.user_permission_tags.get(id=currentTag.id), i
          else:
            profileTagsId.remove(currentTag.id)

        currentTag = currentTag.child
        i -= 1

      return None, -1
    except:
      return None, -1

  def hasPermission(self, permission_codename):
    try:
      PermissionLog.objects.create(
          user=self.user, permission_codename=permission_codename)
      permissions = self.getAllPermissions()
      permissionsCodename = [item.codename for item in permissions]
      if permission_codename in permissionsCodename:
        return True
      else:
        return False
    except:
      return False

  def getAllPermissions(self):
    permissions = set()
    tags = self.user_permission_tags.all()
    for tag in tags:
      for permission in tag.permissions.all():
        permissions.add(permission)
    return permissions

  def getProfileByUserName(user):
    try:
      return Profile.objects.get(user__username=user.username)
    except:
      return None
