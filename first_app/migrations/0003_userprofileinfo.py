# Generated by Django 3.1.2 on 2020-11-08 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first_app', '0002_auto_20201108_0726'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=264, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='email address')),
                ('roles', models.CharField(choices=[('SUPER_ADMIN', 'Super User'), ('ORG_USERS', ' users')], default='ENTITY_ADMIN', max_length=264)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]