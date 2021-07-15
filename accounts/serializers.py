from courses.models import Course
from rest_framework import serializers
from django.contrib.auth import get_user_model
from courses.serializers import CourseSerializer
User = get_user_model()


class ProfileSerializer(serializers.Serializer):
    role = serializers.SerializerMethodField(read_only=True)
    courses = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            'role',
            'username',
            'fullname',
            'courses'
        )

    def get_role(self, obj):
        if obj.is_student:
            return "Student"
        if obj.is_instructor:
            return "Instructor"

    def get_courses(self, obj):
        request = self.context.get('request')
        if obj.is_student:
            all_enrolled = obj.student.enrolled.all()
            count = all_enrolled.count()
            data = {
                'total': count,
                'courses': CourseSerializer(all_enrolled, many=True, context={'request': request}).data
            }
            return data
        if obj.is_instructor:
            all_courses = obj.instructor.course_set.all()
            count = all_courses.count()
            data = {
                'total': count,
                'courses': CourseSerializer(all_courses, many=True, context={'request': request}).data
            }
            return data
