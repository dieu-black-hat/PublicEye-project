# Generated by Django 5.1.2 on 2024-12-03 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.crimereport'),
        ),
    ]