from django.db import models
from accounts.models import Instructor, Student


class Course(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    enrolled = models.ManyToManyField(
        Student, blank=True, related_name="enrolled")

    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.title
