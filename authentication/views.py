from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authentication import BasicAuthentication
from .serializers import InstructorRegisterSerializer, StudentRegisterSerializer
from django.contrib.auth import logout

User = get_user_model()
# Create your views here.

# class AuthAPIView(APIView):
#     def post(self,request,*args,**kwargs):
#         if request.user.is_authenticated:
#             return Response({"Detail":"You are already authenticated"},status=400)
#         data = request.data
#         username = data.get('username')
#         password = data.get('password')
#         user    =  authenticate(username,password)
#         if user:
#             if user.check_password(password):


class InstructorRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    authentication_classes = [BasicAuthentication]
    serializer_class = InstructorRegisterSerializer

    def get_serialzier_context(self, *args, **kwargs):
        return {'request': self.request}

    def get(self, request, *args, **kwargs):
        return Response({'detail': 'Get Method not allowed here'})


class StudentRegisterAPIView(InstructorRegisterAPIView):
    serializer_class = StudentRegisterSerializer


class LogOutAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated)
    authentication_classes = (BasicAuthentication)

    def post(self, request):
        logout(request)
        return
