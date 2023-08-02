# Generated by Django 4.2.3 on 2023-07-30 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_schoollevel_number_of_years'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='fatherPhoneNumber',
            new_name='father_phone_number',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='motherPhoneNumber',
            new_name='mobile_follow_up_on_WhatsApp',
        ),
        migrations.AddField(
            model_name='profile',
            name='mother_phone_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='deaconess',
            field=models.CharField(choices=[('أغس', 'أغنسطس'), ('إبس', 'إبسالطس')], max_length=3),
        ),
    ]