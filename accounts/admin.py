from django.contrib import admin
from .models import User
from .models import Instructor, Student
# Register your models here.

admin.site.register(User)


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
