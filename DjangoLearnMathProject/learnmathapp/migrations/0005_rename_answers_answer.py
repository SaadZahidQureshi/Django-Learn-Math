# Generated by Django 5.0 on 2024-01-22 13:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminDashboard', '0012_alter_question_correct_answer'),
        ('learnmathapp', '0004_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answers',
            new_name='Answer',
        ),
    ]
