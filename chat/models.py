from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='Default description')
    group = models.ForeignKey(Group, related_name='rooms', on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username}: {self.content[:50]}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return self.user.username
