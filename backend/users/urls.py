from django.urls import path
from .views import *

urlpatterns = [
    path('user-info', UserInfoView.as_view(), name='user info')
]
