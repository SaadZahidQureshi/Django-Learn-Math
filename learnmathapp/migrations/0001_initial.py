# Generated by Django 5.0 on 2023-12-26 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserVerification',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('userverification_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('otp', models.IntegerField()),
                ('is_verified', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=100)),
                ('user_image_url', models.URLField(null=True)),
                ('is_active', models.BooleanField()),
                ('is_admin', models.BooleanField(default=False)),
                ('is_verified', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learnmathapp.userverification')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]