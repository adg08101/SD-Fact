# Generated by Django 3.2.4 on 2021-07-08 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fact', '0034_auto_20210707_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='test',
        ),
    ]
