# Generated by Django 3.2.4 on 2021-06-30 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fact', '0009_alter_tasktype_task_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='fact.tasktype'),
        ),
    ]