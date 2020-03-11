from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from starter.app.serializers import UserSerializer, GroupSerializer
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAssigned


class UserViewSet(viewsets.ModelViewSet):
 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
 
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAssigned]