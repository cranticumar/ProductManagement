'''
Created on Feb 1, 2016

@author: bkranthi
'''
from .views import UserViewSet
from rest_framework import routers

views = {
    'users': UserViewSet
}

adminrouter = routers.DefaultRouter()
adminrouter.register(r'users', UserViewSet)