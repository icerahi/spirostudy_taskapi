# Generated by Django 3.2 on 2021-07-15 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='instructor',
            new_name='user',
        ),
    ]
