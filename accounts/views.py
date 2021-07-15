from django.shortcuts import render
from .serializers import ProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

User = get_user_model()


class ProfileAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

    def get_serializer_context(self):
        return {'request': self.request}
