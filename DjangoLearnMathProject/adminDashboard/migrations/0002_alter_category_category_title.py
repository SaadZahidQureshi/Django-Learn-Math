# Generated by Django 5.0 on 2024-01-11 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminDashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_title',
            field=models.CharField(choices=[('Calculus', 'Calculus'), ('Geometery', 'Geometery'), ('Trigonometery', 'Trigonometery'), ('Algebra', 'Algebra')], max_length=100),
        ),
    ]
