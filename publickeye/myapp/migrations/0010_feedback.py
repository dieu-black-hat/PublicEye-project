# Generated by Django 5.1.2 on 2024-11-15 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_crimecategories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('FeedbackID', models.AutoField(primary_key=True, serialize=False)),
                ('Rating', models.IntegerField()),
                ('Comments', models.TextField(blank=True, null=True)),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('ReportID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.report')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usersandadmins')),
            ],
        ),
    ]