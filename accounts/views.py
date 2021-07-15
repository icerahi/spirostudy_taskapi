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
        print(user)
        profile = User.objects.get(username=user.username)
        print(profile)
        serializer = ProfileSerializer(profile, context={'request': request})
        print(serializer.data)
        return Response({"message": "Get reqeust", "profile": serializer.data})
