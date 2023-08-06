from django.db import models

import uuid

from .profileModel import Profile


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
