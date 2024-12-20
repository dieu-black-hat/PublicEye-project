# Generated by Django 5.1.2 on 2024-11-15 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_attachments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('AnalyticsID', models.AutoField(primary_key=True, serialize=False)),
                ('TotalReports', models.IntegerField(default=0)),
                ('ResolvedReports', models.IntegerField(default=0)),
                ('PendingReports', models.IntegerField(default=0)),
                ('DateRange', models.DateField()),
            ],
        ),
    ]
