# Generated by Django 5.1.2 on 2024-11-15 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_analytics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('ResourceID', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Link', models.URLField(max_length=500)),
            ],
        ),
    ]