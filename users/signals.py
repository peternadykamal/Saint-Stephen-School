from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
import users.models as models


# We make this signal to trigger any time user added make for it a profile


@receiver(post_save, sender=User)
def profileUpdated(sender, instance, created, **kwargs):
  # Here we make sure if he want to edit or new user
  if created:
    # The instance is the user the trigger this save function
    user = instance
    profile = models.Profile.objects.create(
        user=user
    )


# if for some reason an admin decides to delete a profile but they forget to delete the user?
# In this case, the user would stay.

@receiver(post_delete, sender=models.Profile)
# Here we remove created argument because if we deleting user we insure it is exist
def deleteProfile(sender, instance, **kwargs):
  # Get the user in the profile that we will delete it
  user = instance.user
  user.delete()
