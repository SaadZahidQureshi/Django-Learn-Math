# Generated by Django 5.0 on 2024-01-24 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminDashboard', '0013_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='time_taken',
            field=models.CharField(default=datetime.datetime(2024, 1, 24, 13, 17, 55, 569880, tzinfo=datetime.timezone.utc), max_length=255),
            preserve_default=False,
        ),
    ]
