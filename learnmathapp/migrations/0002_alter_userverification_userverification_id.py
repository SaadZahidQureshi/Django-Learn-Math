# Generated by Django 5.0 on 2023-12-26 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnmathapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userverification',
            name='userverification_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]