# Generated by Django 5.0 on 2024-01-19 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminDashboard', '0009_alter_question_question_countdown_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_title',
            field=models.TextField(),
        ),
    ]
