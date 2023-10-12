import os

from django.core.management import call_command
from django.db import migrations


def load_fixture(apps, schema_editor):
  fixture_path = os.path.join(os.path.dirname(
      __file__), 'fixtures', 'TalmzaLevelData.json')
  call_command("loaddata", fixture_path)


def unload_fixture(apps, schema_editor):
  # Define the app and model for the fixture you want to delete
  app_label = 'users'
  model_name = 'TalmzaLevel'

  # Delete the data using the model's manager
  Model = apps.get_model(app_label, model_name)
  Model.objects.all().delete()


class Migration(migrations.Migration):

  dependencies = [
      ("users", "0003_load_schoollevel_data"),
  ]

  operations = [migrations.RunPython(
      load_fixture, reverse_code=unload_fixture),]
