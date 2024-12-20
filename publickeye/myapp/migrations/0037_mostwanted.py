# Generated by Django 5.1.2 on 2024-11-23 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_alter_crimereport_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MostWanted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('crime_type', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='most_wanted_images/')),
                ('reward', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Most Wanted',
                'verbose_name_plural': 'Most Wanted',
                'ordering': ['-created_at'],
            },
        ),
    ]