import datetime

from django import forms
from django.contrib.auth.models import Permission
from django.forms import DateField, ModelForm, ValidationError

from users.models.PermissionLogModel import PermissionLog

from . import models


class ProfileForm(ModelForm):
  class Meta:
    model = models.Profile
    fields = ['name', 'birthdate',
              'talmza_level', 'current_talmza_level_year',
              'school_level', 'current_school_level_year',
              'job', 'gender', 'phone_number',
              'father_phone_number', 'mother_phone_number',
              'mobile_follow_up_on_WhatsApp', 'confession_father',
              'church', 'deaconess', 'profile_image'
              ]

  def __init__(self, *args, **kwargs):
    super(ProfileForm, self).__init__(*args, **kwargs)

    field_labels = {
        'name': "الأسم رباعي",
        'birthdate': "تاريخ الميلاد",
        'talmza_level': "مستوى الدراسة في التلمذة",
        'current_talmza_level_year': "سنة الدراسية في التلمذة",
        'school_level': "المرحلة الدراسية",
        'current_school_level_year': "السنة الدراسية",
        'job': "الوظيفة",
        'gender': "النوع",
        'phone_number': "موبايل الملتحق",
        'mobile_follow_up_on_WhatsApp': "موبايل المتابعة علي الواتساب",
        'father_phone_number': "موبايل الأب",
        'mother_phone_number': "موبايل الأم",
        'confession_father': "أب الاعتراف",
        'church': "كنيسته",
        'deaconess': "بيانات خاصة بالرسامة",
        'profile_image': "صورة الملف الشخصي"
    }

    for name, field in self.fields.items():
      field.widget.attrs.update({'class': 'form-control'})
      field.label = field_labels[name]

  def clean_name(self):
    name = self.cleaned_data.get('name')
    if name:
      # Count the number of words in the name
      num_words = len(name.split())
      if num_words != 4:
        raise ValidationError(
            "يجب أن يتكون الاسم من أربع اسماء.")
      # profile = models.Profile.objects.filter(name__iexact=name)
      # if profile:
      #   raise ValidationError("الملف الشخصي بهذا الاسم موجود بالفعل.")
    return name

  def clean_birthdate(self):
    birthdate = self.cleaned_data.get('birthdate')
    if birthdate:
      # Calculate the minimum and maximum birthdates allowed
      today = datetime.date.today().replace(month=10, day=1)
      min_birthdate = (
          today - datetime.timedelta(days=(3.5 * 365))).replace(day=1)
      max_birthdate = today - datetime.timedelta(days=(99 * 365))

      if not max_birthdate <= birthdate <= min_birthdate:
        raise ValidationError(
            "يجب أن يكون تاريخ الميلاد بين 3.5 سنة وأقل من 99 سنة."
        )
    return birthdate

  def clean_current_talmza_level_year(self):
    talmza_level = self.cleaned_data.get(
        'talmza_level')
    current_talmza_level_year = self.cleaned_data.get(
        'current_talmza_level_year')
    if current_talmza_level_year and not (1 <= current_talmza_level_year <= talmza_level.number_of_years):
      raise ValidationError(
          f"يجب أن تكون سنة المستوي 1 أو {talmza_level.number_of_years}.")
    return current_talmza_level_year

  def clean_current_school_level_year(self):
    school_level = self.cleaned_data.get(
        'school_level')
    current_school_level_year = self.cleaned_data.get(
        'current_school_level_year')
    if current_school_level_year and not (1 <= current_school_level_year <= school_level.number_of_years):
      raise ValidationError(
          f"يجب أن تكون سنة الدراسية 1 أو {school_level.number_of_years}.")
    return current_school_level_year

  def validate_phone_number(self, phone_number, field_name):
    if not str(phone_number).isdigit() and phone_number:
      raise ValidationError(
          f"أدخل بيانات صحيحة.")

    if phone_number and (len(phone_number) != 11 or not phone_number.startswith(('010', '011', '012', '015'))):
      # raise ValidationError(
      #     f"{field_name} يجب أن يتكون من 11 رقمًا بالضبط وأن يبدأ بـ '010' أو '011' أو '012' أو '015'.")
      raise ValidationError(
          f"أدخل بيانات صحيحة.")
    return phone_number

  def clean_phone_number(self):
    phone_number = self.cleaned_data.get('phone_number')
    return self.validate_phone_number(phone_number, "موبايل الملتحق")

  def clean_father_phone_number(self):
    father_phone_number = self.cleaned_data.get('father_phone_number')
    return self.validate_phone_number(father_phone_number, "موبايل الأب")

  def clean_mother_phone_number(self):
    mother_phone_number = self.cleaned_data.get('mother_phone_number')
    return self.validate_phone_number(mother_phone_number, "موبايل الأم")

  def clean_mobile_follow_up_on_WhatsApp(self):
    mobile_follow_up_on_WhatsApp = self.cleaned_data.get(
        'mobile_follow_up_on_WhatsApp')
    return self.validate_phone_number(mobile_follow_up_on_WhatsApp, "موبايل المتابعة علي الواتساب")

  birthdate = DateField(
      error_messages={
          'invalid': 'الرجاء إدخال تاريخ ميلاد صالح بالصيغة YYYY-MM-DD.',
      }
  )


class UserPermissionTagForm(ModelForm):
  permissions = forms.ModelMultipleChoiceField(
      queryset=Permission.objects.none(),
      widget=forms.CheckboxSelectMultiple,
      required=False,
  )

  class Meta:
    model = models.UserPermissionTag
    fields = ['tag_name', 'permissions']
    error_messages = {
        'tag_name': {
            'required': 'يرجاء إدخال اسم الوسم.',
            'unique': 'اسم الوسم موجود بالفعل.',
        },
        'permissions': {
            'required': 'يرجاء إختيار صلاحية واحدة على الأقل.',
        },
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # Get a list of permission IDs that have been checked in the logs
    logged_permission_ids = PermissionLog.objects.values_list(
        'permission__id', flat=True)

    # Filter the queryset to include only the permissions that have been logged
    permissions_queryset = Permission.objects.filter(
        id__in=logged_permission_ids)

    # Update the permissions field queryset
    self.fields['permissions'].queryset = permissions_queryset

    # set the permissions field choices format
    permissions_choices = [
        (permission.id, permission.name) for permission in self.fields['permissions'].queryset.all()
    ]
    self.fields['permissions'].choices = permissions_choices

    if self.instance:
      permissions_choices = [
          (permission.id, permission.name) for permission in self.instance.permissions.all()
      ]
      self.fields['permissions'].initial = permissions_choices
      self.tag_id = self.instance.id

  def clean(self):
    cleaned_data = super().clean()

    # Retrieve the existing instance
    instance = getattr(self, 'instance', None)
    # Check if the tag name is being changed and it's not the first or last tag
    if instance and 'tag_name' in cleaned_data:
      new_tag_name = cleaned_data['tag_name']
      if instance.is_top or instance.is_buttom:
        if new_tag_name != instance.tag_name:
          raise forms.ValidationError(
              {"tag_name": "لا يمكن تغير اسم الوسم الأول أو الأخير."}
          )
    # Check if selected permissions already exist
    selected_permissions = cleaned_data.get('permissions')
    # this
    if selected_permissions:
      existing_permissions = Permission.objects.filter(
          id__in=[perm.id for perm in selected_permissions]
      )
      if len(existing_permissions) != len(selected_permissions):
        print('some permissions do not exist')
        raise forms.ValidationError(
            {"permissions": "بعض الصلاحيات غير موجودة."}
        )

    return cleaned_data
