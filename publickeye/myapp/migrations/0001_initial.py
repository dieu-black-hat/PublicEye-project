# Generated by Django 5.1.2 on 2024-11-14 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('OfficerID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Phone', models.CharField(max_length=15)),
                ('Specialization', models.CharField(max_length=100)),
                ('AssignedReports', models.TextField(blank=True)),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('UpdatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
