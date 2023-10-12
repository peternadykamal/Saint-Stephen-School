from django import forms
from django.contrib.auth.models import Permission
from django.forms import ModelForm

from users import models


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
    logged_permission_ids = models.PermissionLog.objects.values_list(
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
