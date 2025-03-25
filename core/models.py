from django.db import models
    
TASK_STATUS = [

    ('pending', 'Pending'),
    ('active', 'Active'),
    ('Completed', 'Completed'),
]

# User Model
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
    
# Tasks Model
class Tasks(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=100)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS, default='pending')

    assigned_users = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.name    