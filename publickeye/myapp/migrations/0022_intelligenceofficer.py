# Generated by Django 5.1.2 on 2024-11-18 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_crimereport_remove_adminlogs_userid_delete_analytics_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntelligenceOfficer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('assigned_crime_type', models.CharField(choices=[('theft', 'Theft'), ('assault', 'Assault'), ('vandalism', 'Vandalism'), ('fraud', 'Fraud')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
