from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class InstructorRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(
        write_only=True, style={'input_type': 'password'})
    message = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'password2',
            'message')

    def get_message(self, obj):
        return f'Thanks for Registration! Please Complete Your Profile!'

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.pop('password2')
        if pw != pw2:
            raise serializers.ValidationError("Password musk match!")
        return data

    def create(self, validated_data):
        user_obj = User(username=validated_data.get('username'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.is_instructor = True
        user_obj.save()
        return user_obj


class StudentRegisterSerializer(InstructorRegisterSerializer):
    def create(self, validated_data):
        user_obj = User(username=validated_data.get('username'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.is_student = True
        user_obj.save()
        return user_obj
