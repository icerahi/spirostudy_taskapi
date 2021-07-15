from rest_framework import serializers
from .models import Course
from rest_framework.reverse import reverse as drf_reverse


class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.SerializerMethodField(read_only=True)
    enroll_now = serializers.SerializerMethodField(read_only=True)
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        extra_fields = ('uri', 'instructor', 'enroll_now')
        read_only_fields = ('instructor',)

    def get_uri(self, obj):
        request = self.context.get('request')
        return drf_reverse('courses:course', kwargs={'pk': obj.pk}, request=request)

    def get_instructor(self, obj):
        return obj.instructor.user.username

    def get_enroll_now(self, obj):
        request = self.context.get('request')
        if request.user.is_student:
            if obj.enrolled.filter(user=request.user).exists():
                return "enrolled"
            return drf_reverse('courses:enroll', kwargs={'pk': obj.pk}, request=request)
        return "You Instructor"
