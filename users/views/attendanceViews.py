import re

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from decorators.checkPermissionDecorator import has_permission_tag
from users import models
from users.forms import AttendanceForm


@ login_required(login_url='sign-in')
@ has_permission_tag(tag_name='admin')
def attendanceForm(request):
  context = {'request': request}

  if request.method == 'POST':
    form = AttendanceForm(request.POST)
    if form.is_valid():
      # Save the form data if it's valid
      form.save()
      taken_profile_attendance = form.instance.profile
      messages.success(
          request, f'تم تسجيل حضور {taken_profile_attendance.name} بنجاح', extra_tags='toast')
      return redirect('attendance_form')
  else:
    form = AttendanceForm()

  context['form'] = form
  return render(request, 'users/attendanceForm.html', context=context)
