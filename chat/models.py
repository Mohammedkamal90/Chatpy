from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Message(models.Model):
    group = models.ForeignKey(Group, related_name='messages', on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE, default=1)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set a default group if not provided
        if not self.group_id:
            default_group = Group.objects.first()
            self.group = default_group

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return self.user.username
