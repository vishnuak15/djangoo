# Generated by Django 3.1.2 on 2020-11-09 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first_app', '0008_userprofileinfo_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='password',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]