# Generated by Django 4.0.5 on 2022-06-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0004_alter_task_completed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]