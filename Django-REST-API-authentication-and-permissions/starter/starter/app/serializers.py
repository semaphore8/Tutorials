from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    assigned_to = serializers.StringRelatedField()
    class Meta:
        model = Task
        fields = ['url', 'id', 'title', 'summary', 'assigned_to']