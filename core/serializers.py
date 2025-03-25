from rest_framework import serializers
from .models import User, Tasks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class Tasks_Serializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)
    # Task are Listed by unique Id's
    assigned_user_ids = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, write_only=True, source='assigned_users'
    )

    class Meta:
        model = Tasks
        fields = ['id', 'name', 'description', 'created_at', 'task_type', 'completed_at', 'status', 'assigned_users', 'assigned_user_ids']
