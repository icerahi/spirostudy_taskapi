from django.shortcuts import render
from .serializers import ProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
User = get_user_model()


# class ProfileAPIView(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = ProfileSerializer
#     queryset = User.objects.all()
#     lookup_field = 'username'

#     def get_serializer_context(self):
#         return {'request': self.request}

class ProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def get(self, request):
        user = request.user
        profile = User.objects.get(username=user.username)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response({"profile": serializer.data})

    def post(self,request):
        return Response({'detail':'Post Method not allowed here'})
