# Generated by Django 4.2.4 on 2023-08-06 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_user_permission_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpermissiontag',
            name='next_Tag',
        ),
        migrations.RemoveField(
            model_name='userpermissiontag',
            name='previous_Tag',
        ),
        migrations.AddField(
            model_name='userpermissiontag',
            name='child',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_tag', to='users.userpermissiontag'),
        ),
        migrations.AddField(
            model_name='userpermissiontag',
            name='parent',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_tag', to='users.userpermissiontag'),
        ),
    ]
