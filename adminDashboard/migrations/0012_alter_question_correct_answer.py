# Generated by Django 5.0 on 2024-01-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminDashboard', '0011_alter_question_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1),
        ),
    ]