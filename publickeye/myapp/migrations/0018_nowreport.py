# Generated by Django 5.1.2 on 2024-11-16 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='NowReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=200)),
                ('victims', models.CharField(blank=True, max_length=200)),
                ('crime_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='crime_images/')),
            ],
        ),
    ]
