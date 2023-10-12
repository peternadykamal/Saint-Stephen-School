import datetime

from django import forms
from django.utils import timezone

from users.models import Attendance, Profile


class AttendanceForm(forms.ModelForm):
  username = forms.CharField(max_length=150, required=True, label="Username")
  attendance_date = forms.DateTimeField(initial=timezone.now, widget=forms.DateTimeInput(
      attrs={'type': 'datetime-local', 'step': 'any'}), required=True, label="Date and Time")
  attendance_type = forms.ChoiceField(
      choices=Attendance.ATTENDANCE_CHOICES, required=True, label="Attendance Type")
  status = forms.ChoiceField(
      choices=Attendance.STATUS_CHOICES, required=True, label="Status")

  error_messages_arabic = {
      "profile_does_not_exist": "لا يوجد ملف تعريف بهذا الاسم",
      "attendance_already_exists": "الحضور لهذا المستخدم في هذا التاريخ والنوع موجود بالفعل",
      "attendance_date_not_today": "يمكن أخذ الحضور فقط لتاريخ اليوم",
      "attendance_time_invalid": "يمكن أخذ الحضور بين الساعة 6:00 صباحًا و 8:10 صباحًا",
      "hymn_class_time_invalid": "يمكن أخذ الحضور بعد الساعة 10:30 صباحًا",
  }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    field_labels = {
        'username': "رقم التسجيل",
        'attendance_date': "تاريخ و وقت الحضور",
        'attendance_type': "نوع الحضور",
        'status': "الحالة",
    }

    today = timezone.now()
    start_of_day = today.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = today.replace(hour=23, minute=59, second=59, microsecond=999)

    self.fields['attendance_date'].widget.attrs.update({
        'min': start_of_day.strftime('%Y-%m-%dT%H:%M'),
        'max': end_of_day.strftime('%Y-%m-%dT%H:%M')
    })

    for name, field in self.fields.items():
      field.label = field_labels[name]

  class Meta:
    model = Attendance
    fields = []

  def clean(self):
    cleaned_data = super().clean()
    username = cleaned_data.get("username")
    attendance_date = cleaned_data.get("attendance_date")
    attendance_type = cleaned_data.get("attendance_type")

    # Check if the username exists
    try:
      profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
      self.add_error(
          "username", self.error_messages_arabic["profile_does_not_exist"])
      return cleaned_data

    cleaned_data["profile"] = profile

    # Check if attendance for the user, date, and attendance type already exists
    same_day_attendance_exists = Attendance.objects.filter(
        profile=profile,
        attendance_date__date=attendance_date.date(),
        attendance_type=attendance_type,
    ).exists()

    if same_day_attendance_exists:
      self.add_error(
          "attendance_date", self.error_messages_arabic["attendance_already_exists"])

    # Check if the date part (without time) is today's date
    if attendance_date.date() != timezone.now().date():
      self.add_error("attendance_date",
                     self.error_messages_arabic["attendance_date_not_today"])
      return cleaned_data

    # Check attendance type and set status based on time
    if attendance_type == 'liturgy':
      if attendance_date.time() >= datetime.time(6, 0) and attendance_date.time() <= datetime.time(8, 10):
        cleaned_data["status"] = 'attendance'
      elif attendance_date.time() > datetime.time(8, 10):
        cleaned_data["status"] = "late"
      else:
        self.add_error(
            "attendance_date", self.error_messages_arabic["attendance_time_invalid"])
    elif attendance_type == 'hymnClass':
      if attendance_date.time() < datetime.time(10, 30):
        self.add_error("attendance_date",
                       self.error_messages_arabic["hymn_class_time_invalid"])

    # save cleaned data in the form.instance without username
    cleaned_data.pop("username")
    self.instance = Attendance(**cleaned_data)

    return cleaned_data
