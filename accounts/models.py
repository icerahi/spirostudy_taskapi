from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# add two extra field for role by inheriting AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)


# Instructor model more field can be add later
class Instructor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.user.username

# Student model more field can be add later


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.user.username

# when a user is created it will check his role and will create object,
# this role will get from register endpoint


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_teacher_or_student(sender, instance, created, **kwargs):
    if created:
        if instance.is_instructor == True:
            Instructor.objects.create(user=instance)
        if instance.is_student == True:
            Student.objects.create(user=instance)
