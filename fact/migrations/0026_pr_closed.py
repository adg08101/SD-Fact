# Generated by Django 3.2.4 on 2021-07-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fact', '0025_pr_responsable'),
    ]

    operations = [
        migrations.AddField(
            model_name='pr',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
