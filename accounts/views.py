from django.shortcuts import render
from .serializers import ProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
User = get_user_model()


 
class ProfileAPIView(APIView):

    def get(self, request):
        user = request.user
        profile = User.objects.get(username=user.username)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response({"profile": serializer.data})

    def post(self,request):
        return Response({'detail':'Post Method not allowed here'})
