from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from .profileModel import Profile


class Attendance(models.Model):
  ATTENDANCE_CHOICES = (
      ('liturgy', 'القداس'),
      ('hymnClass', 'حصة الألحان'),
  )

  STATUS_CHOICES = (
      ('attendance', 'حضور'),
      ('late', 'تأخير'),
  )

  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  attendance_date = models.DateTimeField(default=timezone.now, null=False)
  attendance_type = models.CharField(
      max_length=50, choices=ATTENDANCE_CHOICES, default=ATTENDANCE_CHOICES[0][0], null=False)
  status = models.CharField(
      max_length=50, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], null=False)

  class Meta:
    unique_together = ('profile', 'attendance_date', 'attendance_type')

  def __str__(self):
    return f'{self.profile.user.username} - {self.attendance_date} - {self.attendance_type} - {self.status}'
