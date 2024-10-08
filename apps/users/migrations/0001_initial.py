# Generated by Django 5.0.7 on 2024-08-09 06:45

import citext.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=30, validators=[django.core.validators.MinLengthValidator(2, 'First name must be at least 2 characters long.')], verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=30, validators=[django.core.validators.MinLengthValidator(2, 'Last name must be at least 2 characters long.')], verbose_name='Last name')),
                ('email', citext.fields.CIEmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='Staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active.', verbose_name='Active')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions.', verbose_name='Superuser')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='Deleted at')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
