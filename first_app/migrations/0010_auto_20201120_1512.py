# Generated by Django 3.1.2 on 2020-11-20 15:12

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0009_auto_20201109_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='contact_no',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
