# Generated by Django 4.0.5 on 2022-06-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0003_task_team_teamtomember_taskassignedtomember_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed_at',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]