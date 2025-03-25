from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Tasks
from .serializers import UserSerializer, Tasks_Serializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = Tasks_Serializer
    

    # assigning task to User if user exists 
    @action(detail=True, methods=['post'])
    def assign_users(self, request, pk=None):
        task = self.get_object()
        user_ids = request.data.get('user_ids', [])
        users = User.objects.filter(id__in=user_ids)
        if not users.exists():
            return Response({'error': 'User Not Exist.'}, status=status.HTTP_400_BAD_REQUEST)
        
        task.assigned_users.set(users)
        task.save()
        return Response({'status': 'Users assigned successfully'}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # view to see the task assigned to users
    @action(detail=True, methods=['get'])
    def tasks(self, request, pk=None):
        user = self.get_object()
        tasks = user.tasks.all()
        serializer = Tasks_Serializer(tasks, many=True)
        return Response(serializer.data)
