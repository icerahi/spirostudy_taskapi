# Generated by Django 3.2 on 2021-07-15 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_rename_user_course_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
