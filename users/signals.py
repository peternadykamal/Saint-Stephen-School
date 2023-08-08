from email.policy import default
from os import name
import profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
import users.models as models

import datetime
import os


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
    os.remove(image_path)
  if instance.address:
    instance.address.delete()
  # TODO delete his all expenses for all years
  user = instance.user
  user.delete()
