from django.db import models

import uuid


class SchoolLevel(models.Model):
  level_name = models.CharField(max_length=50)
  level_number = models.IntegerField()
  number_of_years = models.IntegerField(null=True, blank=True)
  next_level = models.OneToOneField(
      "SchoolLevel", related_name="school_next_level", on_delete=models.SET_NULL, null=True, blank=True)
  previous_level = models.OneToOneField(
      "SchoolLevel", related_name="school_previous_level", on_delete=models.SET_NULL, null=True, blank=True)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  class Meta:
    ordering = ['level_number']

  def __str__(self):
    return str(self.level_name)
