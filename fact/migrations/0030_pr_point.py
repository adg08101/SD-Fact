# Generated by Django 3.2.4 on 2021-07-08 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fact', '0029_pointingenvironments'),
    ]

    operations = [
        migrations.AddField(
            model_name='pr',
            name='point',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='fact.pointingenvironments'),
        ),
    ]
