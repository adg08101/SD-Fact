# Generated by Django 3.2.4 on 2021-07-08 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fact', '0033_pr_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pr',
            name='test',
        ),
        migrations.AddField(
            model_name='task',
            name='test',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
