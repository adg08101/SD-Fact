# Generated by Django 3.2.4 on 2021-07-06 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fact', '0024_alter_responsable_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pr',
            name='responsable',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='fact.responsable'),
        ),
    ]
