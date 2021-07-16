from rest_framework import permissions
from .models import Course
from django.core.exceptions import ObjectDoesNotExist


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = "You must be the creator of this course to edit"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_instructor and request.user.instructor == obj.instructor:
            return True


class StudentEnrollOnly(permissions.BasePermission):
    message = "You have you to be a student to enroll this course!"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # only student can enroll course
        if obj.instructor == request.user.Instructor:
            return True


class IsOwnerAccessOnly(permissions.BasePermission):
    message = " Creator of this course make it as inactive"

    def has_object_permission(self, request, view, obj):
        # accesss for all if course is active
        if obj.active == True:
            return True

        # when course inactive then restrict from others
        if obj.active == False and request.user.is_instructor and request.user.instructor == obj.instructor:
            return True
