# Generated by Django 5.1.2 on 2024-11-23 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_remove_crimereport_report_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='crimereport',
            options={'ordering': ['-created_at'], 'verbose_name': 'Crime Report', 'verbose_name_plural': 'Crime Reports'},
        ),
        migrations.AddField(
            model_name='crimereport',
            name='report_id',
            field=models.CharField(default='', editable=False, max_length=20, unique=True),
        ),
    ]
