from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from .permissions import IsOwnerOrReadOnly, IsOwnerAccessOnly, StudentEnrollOnly
from .models import Course
from .serializers import CourseSerializer
from rest_framework.authentication import BasicAuthentication
from django.shortcuts import get_object_or_404


class CourseDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly, IsOwnerAccessOnly]  # our custom permissions classes
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CourseListAndCreateAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    # filtering all active courses
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer

    def post(self, request, *args, **kwargs):
        # only instructor role user can create course
        if request.user.is_instructor:
            return self.create(request, *args, **kwargs)
        return Response({'detail': 'You must be a Instructor to create course!!'})

    def perform_create(self, serializer):
        # setting current user as instructor
        serializer.save(instructor=self.request.user.instructor)


# course enroll api view, only student can able to enroll course
class CourseEnrollAPIView(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_student:
            course_id = self.kwargs.get('pk')
            course = get_object_or_404(Course, pk=course_id)
            course.enrolled.add(request.user.student)
            return Response({'detail': "You have enrolled!"})
        return Response({'detail': 'You have to be a student to enroll course'})
