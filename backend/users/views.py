from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import MyUserSerializer
# Create your views here.

class UserInfoView(RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = MyUserSerializer
    
    def get_object(self):
        return self.request.user
