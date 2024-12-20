# Generated by Django 5.1.2 on 2024-11-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_reportedcrime'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=255)),
                ('victims', models.CharField(blank=True, max_length=255)),
                ('crime_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='crime_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='adminlogs',
            name='UserID',
        ),
        migrations.DeleteModel(
            name='Analytics',
        ),
        migrations.RemoveField(
            model_name='attachments',
            name='ReportID',
        ),
        migrations.RemoveField(
            model_name='case',
            name='OfficerID',
        ),
        migrations.RemoveField(
            model_name='case',
            name='ReportID',
        ),
        migrations.DeleteModel(
            name='CrimeCategories',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='ReportID',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='UserID',
        ),
        migrations.DeleteModel(
            name='MostWanted',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='UserID',
        ),
        migrations.DeleteModel(
            name='NowReport',
        ),
        migrations.DeleteModel(
            name='Officer',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='ReportID',
        ),
        migrations.RemoveField(
            model_name='report',
            name='UserID',
        ),
        migrations.DeleteModel(
            name='ReportedCrime',
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
        migrations.DeleteModel(
            name='UserRoles',
        ),
        migrations.DeleteModel(
            name='AdminLogs',
        ),
        migrations.DeleteModel(
            name='Attachments',
        ),
        migrations.DeleteModel(
            name='Case',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='Notifications',
        ),
        migrations.DeleteModel(
            name='Progress',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.DeleteModel(
            name='UsersAndAdmins',
        ),
    ]