# Generated by Django 3.2.4 on 2021-06-30 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sprint',
            old_name='number',
            new_name='sprint_number',
        ),
    ]
