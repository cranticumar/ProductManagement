'''
Created on Feb 1, 2016

@author: bkranthi
'''
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer