from rest_framework.serializers import ModelSerializer
from .models import MyUser


class MyUserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields= ['username', 'email', 'first_name', 'last_name']