# Generated by Django 4.0.5 on 2022-06-18 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0007_alter_teamtomember_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='teamtomember',
            unique_together=set(),
        ),
    ]
