from django.db import models

# Create your models here.
from main.models import Users


class Chats(models.Model):
    first_user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='first_name')
    second_user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='second_name')
    created_date = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chats, on_delete=models.CASCADE)
    sender = models.ForeignKey(Users, on_delete = models.SET_NULL, null=True, related_name='sender')
    recipient = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='recipient')
    message = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)
