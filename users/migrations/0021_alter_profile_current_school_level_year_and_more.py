# Generated by Django 4.2.4 on 2023-08-02 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_profile_school_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='current_school_level_year',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'ذكر'), ('F', 'أنثي')], max_length=1),
        ),
    ]
