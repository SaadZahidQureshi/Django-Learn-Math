# Generated by Django 5.0 on 2024-01-29 07:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminDashboard', '0016_alter_answer_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='adminDashboard.question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='level',
            name='level_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='adminDashboard.category'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='adminDashboard.level'),
        ),
    ]