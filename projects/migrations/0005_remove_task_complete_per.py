# Generated by Django 2.0.3 on 2021-10-26 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_task_complete_per'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='complete_per',
        ),
    ]