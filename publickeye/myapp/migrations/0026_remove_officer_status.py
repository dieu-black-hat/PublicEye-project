# Generated by Django 5.1.2 on 2024-11-19 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_officer_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officer',
            name='status',
        ),
    ]
