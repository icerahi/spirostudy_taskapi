# Generated by Django 3.2 on 2021-07-15 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_instructor_student'),
        ('courses', '0004_alter_course_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='enrolled',
            field=models.ManyToManyField(blank=True, related_name='enrolled', to='accounts.Student'),
        ),
    ]