# Generated by Django 4.0.5 on 2023-02-01 20:49

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
