from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = "You must be the creator of this course to edit"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.instructor == request.user:
            return True

class StudentEnrollOnly(permissions.BasePermission):
    message = "You have you to be a student to enroll this course!"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.instructor == request.user:
            return True
