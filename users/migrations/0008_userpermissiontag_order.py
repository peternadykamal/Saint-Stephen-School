# Generated by Django 4.2.4 on 2023-09-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_remove_profile_highest_tag_level"),
    ]

    operations = [
        migrations.AddField(
            model_name="userpermissiontag",
            name="order",
            field=models.IntegerField(default=-1),
        ),
    ]