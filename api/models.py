from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=timezone.now())
    updated_at = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    

