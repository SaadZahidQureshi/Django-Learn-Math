# Generated by Django 5.0.1 on 2024-05-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminDashboard', '0018_remove_level_number_of_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='number_of_questions',
            field=models.IntegerField(default=0),
        ),
    ]
