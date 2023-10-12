import os

from django.core.management import call_command
from django.db import migrations


def load_fixture(apps, schema_editor):
  fixture_path = os.path.join(os.path.dirname(
      __file__), 'fixtures', 'SchoolLevelData.json')
  call_command("loaddata", fixture_path)


def unload_fixture(apps, schema_editor):
  # Define the app and model for the fixture you want to delete
  app_label = 'users'
  model_name = 'SchoolLevel'

  # Delete the data using the model's manager
  Model = apps.get_model(app_label, model_name)
  Model.objects.all().delete()


class Migration(migrations.Migration):

  dependencies = [
      # ("users", "0005_alter_profile_current_talmza_level_year_and_more"),
      ("users", "0002_custom_permissions"),
  ]

  operations = [migrations.RunPython(
      load_fixture, reverse_code=unload_fixture),]
