from django.forms import ModelForm, ValidationError, DateField
from . import models

import datetime


class ProfileForm(ModelForm):
  class Meta:
    model = models.Profile
    fields = '__all__'
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

    for name, field in self.fields.items():
      field.widget.attrs.update({'class': 'form-control'})
      match name:
        case 'name':
          field.label = "الأسم رباعي"
        case 'birthdate':
          field.label = "تاريخ الميلاد"
        case 'talmza_level':
          field.label = "مستوي"
        case 'current_talmza_level_year':
          field.label = "سنة المستوي"
        case 'school_level':
          field.label = "المرحلة الدراسية"
        case 'current_school_level_year':
          field.label = "سنة الدراسية"
        case 'job':
          field.label = "الوظيفة"
        case 'gender':
          field.label = "النوع"
        case 'phone_number':
          field.label = "موبايل الملتحق"
        case 'mobile_follow_up_on_WhatsApp':
          field.label = "موبايل المتابعة علي الواتساب"
        case 'father_phone_number':
          field.label = "موبايل الأب"
        case 'mother_phone_number':
          field.label = "موبايل الأم"
        case 'confession_father':
          field.label = "أب الاعتراف"
        case 'church':
          field.label = "كنيسته"
        case 'deaconess':
          field.label = "الرسامة"
        case 'profile_image':
          field.label = "الصورة الشخصية"

  def clean_name(self):
    name = self.cleaned_data.get('name')
    if name:
      # Count the number of words in the name
      num_words = len(name.split())
      if num_words != 4:
        raise ValidationError(
            "يجب أن يتكون الاسم من أربع اسماء.")
      profile = models.Profile.objects.filter(name__iexact=name)
      if profile:
        raise ValidationError("الملف الشخصي بهذا الاسم موجود بالفعل.")
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
