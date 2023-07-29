from argparse import Action
from ast import mod, pattern
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
  GENDER_CHOICES = (
      ('M', "Male"),
      ('F', "Female")
  )
  DEACONESS_CHOICES = (
      ('أغس', "أغنسطس"),
      ('إبص', "إبصالتس")
  )

  user = models.OneToOneField(
      User, on_delete=models.CASCADE)  # TODO delete user when profile deleted
  name = models.CharField(max_length=200, unique=True)
  birthdate = models.DateField()
  talmza_level = models.ForeignKey(
      "TalmzaLevel", on_delete=models.SET_NULL, null=True, blank=True)
  currentTalmzaLevelYear = models.IntegerField(default=1)
  school_level = models.ForeignKey(
      "SchoolLevel", on_delete=models.SET_NULL, null=True, blank=True)
  currentSchoolLevelYear = models.IntegerField(default=1)
  address = models.OneToOneField(
      "Address", on_delete=models.SET_NULL, null=True, blank=True)
  job = models.CharField(max_length=200, null=True, blank=True)
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
  phone_number = models.CharField(max_length=11, null=True, blank=True)
  fatherPhoneNumber = models.CharField(max_length=11, null=True, blank=True)
  motherPhoneNumber = models.CharField(max_length=11, null=True, blank=True)
  # TODO whatsapp
  confessionFather = models.CharField(max_length=200, null=True, blank=True)
  church = models.CharField(
      max_length=200, default="كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال")
  deaconess = models.CharField(max_length=3, choices=DEACONESS_CHOICES)
  profile_image = models.ImageField(
      null=True, blank=True, upload_to='images/profiles', default='images/profiles/user-default.png')

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return str(self.name)


class Address(models.Model):
  building = models.CharField(max_length=20, null=True, blank=True)
  street = models.CharField(max_length=20, null=True, blank=True)
  branches_from = models.CharField(max_length=20, null=True, blank=True)
  floor = models.CharField(max_length=20, null=True, blank=True)
  apartment_number = models.CharField(max_length=20, null=True, blank=True)
  residential_complexes = models.CharField(
      max_length=20, null=True, blank=True)
  district = models.CharField(max_length=20, null=True, blank=True)
  additional_details = models.CharField(max_length=20, null=True, blank=True)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return str(self.building)


class TalmzaLevel(models.Model):
  level_name = models.CharField(max_length=20)
  level_number = models.IntegerField()
  number_of_years = models.IntegerField(default=2)
  next_level = models.OneToOneField(
      "TalmzaLevel", on_delete=models.SET_NULL, null=True, blank=True)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return str("المستوي " + self.level_name + " # " + str(self.level_number))


class SchoolLevel(models.Model):
  level_name = models.CharField(max_length=20)
  level_number = models.IntegerField()
  number_of_years = models.IntegerField(null=True, blank=True)
  next_level = models.OneToOneField(
      "SchoolLevel", on_delete=models.SET_NULL, null=True, blank=True)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return str("الصف " + self.level_name + " # " + str(self.level_number))


class MasreefProfileForm(models.Model):
  year = models.CharField(max_length=4)
  amount_of_money_payed = models.IntegerField()
  created_for = models.ForeignKey(
      Profile, on_delete=models.SET_NULL, null=True, blank=False)
  # TODO total number of masreef (not as a proprty in the table but an constant stored in a spearte table or as .env file in backend)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return str(self.created_for + " دفع " + str(self.amount_of_money_payed) + "جنيهات")


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
