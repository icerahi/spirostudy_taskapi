from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authentication import BasicAuthentication
from .serializers import InstructorRegisterSerializer, StudentRegisterSerializer
from django.contrib.auth import logout

User = get_user_model()

# instructor registration view


class InstructorRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InstructorRegisterSerializer

    def get_serialzier_context(self, *args, **kwargs):
        return {'request': self.request}

    def get(self, request, *args, **kwargs):
        return Response({'detail': 'Get Method not allowed here'})


# student registration view is inherit from above class
class StudentRegisterAPIView(InstructorRegisterAPIView):
    serializer_class = StudentRegisterSerializer
