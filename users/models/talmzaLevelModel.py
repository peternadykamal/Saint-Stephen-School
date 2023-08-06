from django.db import models

import uuid


class TalmzaLevel(models.Model):
  level_name = models.CharField(max_length=50)
  level_number = models.IntegerField()
  number_of_years = models.IntegerField(default=2)
  next_level = models.OneToOneField(
      "TalmzaLevel", related_name="talmza_next_level", on_delete=models.SET_NULL, null=True, blank=True)
  previous_level = models.OneToOneField(
      "TalmzaLevel", related_name="talmza_previous_level", on_delete=models.SET_NULL, null=True, blank=True)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  class Meta:
    ordering = ['level_number']

  def __str__(self):
    return str(self.level_name)
