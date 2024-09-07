from django.shortcuts import render

from rest_framework import viewsets
from .models import Department, UserProfile
from .serializers import DepartmentSerializer, UserProfileSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

