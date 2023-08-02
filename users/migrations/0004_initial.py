# Generated by Django 4.2.3 on 2023-07-29 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('building', models.CharField(blank=True, max_length=20, null=True)),
                ('street', models.CharField(blank=True, max_length=20, null=True)),
                ('branches_from', models.CharField(blank=True, max_length=20, null=True)),
                ('floor', models.CharField(blank=True, max_length=20, null=True)),
                ('apartment_number', models.CharField(blank=True, max_length=20, null=True)),
                ('residential_complexes', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.CharField(blank=True, max_length=20, null=True)),
                ('additional_details', models.CharField(blank=True, max_length=20, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(max_length=200, unique=True)),
                ('birthdate', models.DateField(default='2000-01-01')),
                ('job', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('fatherPhoneNumber', models.CharField(blank=True, max_length=11, null=True)),
                ('motherPhoneNumber', models.CharField(blank=True, max_length=11, null=True)),
                ('confessionFather', models.CharField(blank=True, max_length=200, null=True)),
                ('church', models.CharField(default='كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال', max_length=200)),
                ('deaconess', models.CharField(choices=[('أغس', 'أغنسطس'), ('إبص', 'إبصالتس')], max_length=3)),
                ('profile_image', models.ImageField(blank=True, default='images/profiles/user-default.png', null=True, upload_to='images/profiles')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]