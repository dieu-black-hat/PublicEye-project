# Generated by Django 5.1.2 on 2024-11-14 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UsersAndAdmins',
        ),
        migrations.AlterModelTable(
            name='usersandadmins',
            table='users_and_admins',
        ),
    ]