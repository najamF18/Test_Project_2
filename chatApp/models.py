from django.db import models
from LoginApp.models import User
# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.message
 
    class Meta:
        ordering = ('timestamp',)
        
class ChatThread(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_user_msg')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_user_msg')
    message = models.ManyToManyField(Message, related_name="thread")
    
    def __str__(self):
        return self.sender.email