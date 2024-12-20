# Generated by Django 5.1.2 on 2024-11-15 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_adminlogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('CaseID', models.AutoField(primary_key=True, serialize=False)),
                ('CaseStatus', models.CharField(max_length=50)),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('UpdatedAt', models.DateTimeField(auto_now=True)),
                ('OfficerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usersandadmins')),
                ('ReportID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.report')),
            ],
        ),
    ]
