from django.db import models
from django.contrib.auth.models import User
class Group(models.Model):
    group_name = models.CharField(max_length=250)
    description = models.CharField(max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name

class ImagePost(models.Model):
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='groupImage/')
    # userId = models.ForeignKey(User, related_name='imagepost', on_delete=models.CASCADE)

    def __str__(self):
        return self.description




class Message(models.Model):
    group = models.ForeignKey(Group, related_name='messages', on_delete=models.CASCADE)
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f'{self.sender}: {self.content[:30]}'
