from django.contrib.auth.models import Permission, User
from django.db import models

# this manager is used to create PermissionLog objects and to override the create method, to make sure that
# the permission that is being checked is a valid permission


class PermissionLogManager(models.Manager):
  def create(self, user, permission_codename):
    permission = Permission.objects.filter(
        codename=permission_codename).first()
    if permission:
      return super().create(user=user, permission=permission)

# here is the reason why i created this model, i needed way to keep track of the permissions that constantly
# checked by the backend in the checkPermissionDecorator.py in has_permission function
# by doing so i can know which permissions are getting checked the most and which are not checked at all
# as i want to show to admin in the tags control panel the permissions that are checked by the backend only


class PermissionLog(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_now_add=True)

  objects = PermissionLogManager()

  def __str__(self):
    return f"{self.user.username} checked permission: {self.permission.codename} at {self.timestamp}"
