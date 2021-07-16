from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from .permissions import IsOwnerOrReadOnly
from .models import Course
from .serializers import CourseSerializer
from rest_framework.authentication import BasicAuthentication
from django.shortcuts import get_object_or_404


class CourseDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [BasicAuthentication]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CourseListAndCreateAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]

    def post(self, request, *args, **kwargs):
        if request.user.is_instructor:
            return self.create(request, *args, **kwargs)
        return Response({'detail': 'You must be a Instructor to create course!!'})

    def perform_create(self, serializer):
        print(serializer.validated_data)
        print(self.request.user)
        serializer.save(instructor=self.request.user.instructor)


class CourseEnrollAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.is_student:
            course_id = self.kwargs.get('pk')
            course = get_object_or_404(Course, pk=course_id)
            course.enrolled.add(request.user.student)
            return Response({'detail': "You have enrolled!"})
        return Response({'detail': 'You have to be a student to enroll course'})
