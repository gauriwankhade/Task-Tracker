# Generated by Django 4.0.5 on 2022-06-18 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0006_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='teamtomember',
            unique_together={('team', 'member')},
        ),
    ]