# Generated by Django 4.2.4 on 2023-08-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_user_permission_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_permission_tags',
            field=models.ManyToManyField(blank=True, null=True, to='users.userpermissiontag'),
        ),
    ]
