# Generated by Django 3.2.4 on 2021-06-30 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fact', '0017_prtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='PR',
            fields=[
                ('pr_number', models.IntegerField(primary_key=True, serialize=False)),
                ('sent', models.BooleanField(default=True)),
                ('merged', models.BooleanField(default=False)),
                ('rolled_back', models.BooleanField(default=False)),
                ('still_open', models.BooleanField(default=False)),
                ('task', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='fact.task')),
                ('type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='fact.prtype')),
            ],
        ),
    ]
