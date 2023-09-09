from django.apps import AppConfig
from django.conf import settings


class UsersConfig(AppConfig):
  default_auto_field = 'django.db.models.BigAutoField'
  name = 'users'

  def ready(self):
    super().ready()
    import users.signals

    # note that media files won't get loaded correctly in the website
    # i can't find a way to fix this, so comment it out when you want to run the website
    if settings.DEBUG:
      import users.tests.quickTest
