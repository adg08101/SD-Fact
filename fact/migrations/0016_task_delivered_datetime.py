# Generated by Django 3.2.4 on 2021-06-30 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fact', '0015_alter_task_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='delivered_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]