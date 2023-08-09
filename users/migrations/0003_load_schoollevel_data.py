from django.db import migrations
from django.core.management import call_command
import os


def load_fixture(apps, schema_editor):
  fixture_path = os.path.join(os.path.dirname(
      __file__), 'fixtures', 'SchoolLevelData.json')
  call_command("loaddata", fixture_path)


class Migration(migrations.Migration):

  dependencies = [
      # ("users", "0005_alter_profile_current_talmza_level_year_and_more"),
      ("users", "0002_custom_permissions"),
  ]

  operations = [migrations.RunPython(load_fixture),]
