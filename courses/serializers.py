from rest_framework import serializers
from .models import Course
from rest_framework.reverse import reverse as drf_reverse


class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.SerializerMethodField(read_only=True)
    enroll_now = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        extra_fields = ('instructor', 'enroll_now')
        read_only_fields = ('instructor',)

    def get_instructor(self, obj):
        return obj.instructor.user.username

    def get_enroll_now(self, obj):
        request = self.context.get('request')
        if request.user != obj.instructor.user:
            return drf_reverse('courses:enroll', kwargs={'pk': obj.pk}, request=request)
        return
