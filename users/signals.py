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
