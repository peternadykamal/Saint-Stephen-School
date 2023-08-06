import select
from django.db import migrations
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


new_permissions = [
    ('view_profile_talmza_level', 'view profile talmza level', 'users', 'profile'),
    ('change_profile_talmza_level', 'change profile talmza level', 'users', 'profile'),
    ('view_profile_current_talmza_level_year',
     'view profile current talmza level', 'users', 'profile'),
    ('change_profile_current_talmza_level_year',
     'change profile current talmza level', 'users', 'profile'),
]


def create_permissions(apps, schema_editor):
  # Create new permissions if they don't exist
  for i in range(len(new_permissions)):
    try:
      if (len(new_permissions[i]) == 4):
        codename, description, app, model = new_permissions[i]
        selectedModel = apps.get_model(app, model)
        content_type = ContentType.objects.get_for_model(selectedModel)
      else:
        content_type = None

      Permission.objects.get_or_create(
          codename=codename, name=description,
          content_type=content_type)
    except:
      pass


def revert_create_permissions(apps, schema_editor):
  # Delete the created permissions (if you want to undo the changes during rollback)
  Permission.objects.filter(
      codename__in=[codename for codename, _ in new_permissions]).delete()


class Migration(migrations.Migration):

  dependencies = [
      ('users', '0001_initial'),
  ]

  operations = [
      migrations.RunPython(create_permissions, revert_create_permissions),
  ]
