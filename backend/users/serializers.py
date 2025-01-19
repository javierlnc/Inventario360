from rest_framework.serializers import ModelSerializer
from .models import MyUser


class MyUserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name']


class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', 'first_name', 'last_name', 'password']
        extra_kwargs = {"password": {'writte_only: True'}}

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
