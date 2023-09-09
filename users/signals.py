import csv
import datetime
import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import (m2m_changed, post_delete, post_save,
                                      pre_delete)
from django.dispatch import receiver

import users.models as models
from users.models.expensesProfileFormModel import ExpensesProfileForm

from .utils import (create_csv_if_not_exists, cropImage, deleteProfileImage,
                    is_image_path_present)

# We make this signal to trigger any time user added make for it a profile


@receiver(post_save, sender=User)
def userUsernameUpdated(sender, instance, created, **kwargs):
  # Here we make sure if he want to edit or new user
  if created:
    # The instance is the user the trigger this save function
    user = instance
    year = datetime.date.today().year   # 2023
    id = user.id
    user.username = str(year % 2000) + f"{id:05d}"
    user.save()

    # profile, _ = models.Profile.objects.get_or_create(
    #     user=user
    # )

# if for some reason an admin decides to delete a profile but they forget to delete the user?
# In this case, the user would stay.


@receiver(post_delete, sender=models.Profile)
# Here we remove created argument because if we deleting user we insure it is exist
def deleteProfile(sender, instance, **kwargs):
  # Get the user in the profile that we will delete it

  image_path = instance.profile_image.path

  # Delete the file from the filesystem if not the default
  if not models.Profile.DEFAULT_PROFILE_PATH.replace('/', '\\') in image_path:
    deleteProfileImage(image_path)
  if instance.address:
    instance.address.delete()
  ExpensesProfileForm.objects.filter(created_for=instance).delete()
  user = instance.user
  user.delete()


@receiver(post_save, sender=models.Profile)
def saveProfile(sender, instance, **kwargs):
  image_path = instance.profile_image.path

  destination_path = settings.ORIGINAL_PROFILE_PICTURES_FOLDER
  # this csv file will contain images that get cropped manually not using the autocropper
  csv_path = settings.MANUALLY_CROPPED_PATHES_CSV

  non_cropped_image_path = os.path.join(
      destination_path, os.path.basename(image_path))
  cropped_image_path = image_path

  if not models.Profile.DEFAULT_PROFILE_PATH.replace('/', '\\') in image_path:
    try:
      cropImage(image_path, destination_path)
    except FileNotFoundError as e:
      # this exception will be raised if the image is not found
      default_image_path = models.Profile.DEFAULT_PROFILE_PATH
      instance.profile_image = default_image_path
      instance.save()
    except Exception as e:
      create_csv_if_not_exists(csv_path)
      if not is_image_path_present(csv_path, image_path):
        with open(csv_path, "a", newline="") as csvfile:
          csv_writer = csv.writer(csvfile)
          csv_writer.writerow([cropped_image_path, non_cropped_image_path])


@receiver(pre_delete, sender=models.UserPermissionTag)
def remove_permission_tag_from_profiles(sender, instance, **kwargs):
    # Get all profiles associated with the instance being deleted
  profiles = models.Profile.objects.filter(user_permission_tags=instance)

  # Remove the instance from each profile's user_permission_tags
  for profile in profiles:
    profile.user_permission_tags.remove(instance)


@receiver(m2m_changed, sender=models.Profile.user_permission_tags.through)
def update_highest_tag(sender, instance, action, pk_set, **kwargs):
  if action == 'post_add' or action == 'post_remove':
    highest_tag = models.UserPermissionTag.get_highest_tag(
        list(instance.user_permission_tags.all()))
    instance.highest_tag = highest_tag
    instance.save()
