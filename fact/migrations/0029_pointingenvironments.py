# Generated by Django 3.2.4 on 2021-07-08 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fact', '0028_pr_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointingEnvironments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(max_length=25, unique=True)),
            ],
        ),
    ]
