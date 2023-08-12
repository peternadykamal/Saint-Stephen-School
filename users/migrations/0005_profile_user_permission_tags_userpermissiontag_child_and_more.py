# Generated by Django 4.2.4 on 2023-08-09 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("users", "0004_load_talmzalevel_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="user_permission_tags",
            field=models.ManyToManyField(blank=True, to="users.userpermissiontag"),
        ),
        migrations.AddField(
            model_name="userpermissiontag",
            name="child",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="child_tag",
                to="users.userpermissiontag",
            ),
        ),
        migrations.AddField(
            model_name="userpermissiontag",
            name="is_buttom",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userpermissiontag",
            name="is_top",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userpermissiontag",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="parent_tag",
                to="users.userpermissiontag",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="current_talmza_level_year",
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="talmza_level",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.talmzalevel",
            ),
        ),
        migrations.AlterField(
            model_name="userpermissiontag",
            name="permissions",
            field=models.ManyToManyField(blank=True, to="auth.permission"),
        ),
    ]