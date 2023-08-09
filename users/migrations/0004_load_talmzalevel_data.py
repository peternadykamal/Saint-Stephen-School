from django.db import migrations
from django.core.management import call_command
import os


def load_fixture(apps, schema_editor):
  fixture_path = os.path.join(os.path.dirname(
      __file__), 'fixtures', 'TalmzaLevelData.json')
  call_command("loaddata", fixture_path)


class Migration(migrations.Migration):

  dependencies = [
      ("users", "0003_load_schoollevel_data"),
  ]

  operations = [migrations.RunPython(load_fixture),]
