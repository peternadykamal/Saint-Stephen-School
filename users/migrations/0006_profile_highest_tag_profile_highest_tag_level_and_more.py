# Generated by Django 4.2.4 on 2023-09-07 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_permissionlog"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="highest_tag",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="profile_with_highest_tag",
                to="users.userpermissiontag",
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="highest_tag_level",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="user_permission_tags",
            field=models.ManyToManyField(
                blank=True,
                related_name="profiles_with_user_permission_tag",
                to="users.userpermissiontag",
            ),
        ),
    ]