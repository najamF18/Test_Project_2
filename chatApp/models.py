from django.db import models
from LoginApp.models import User
# Create your models here.
        
class ChatThread(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_user_msg')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_user_msg')
    
    
    def __str__(self):
        return self.sender.email

class Message(models.Model):
    message = models.CharField(max_length=1200)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_of_msg')
    timestamp = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(ChatThread, on_delete=models.CASCADE, related_name="message_thread")
    
    def __str__(self):
        return self.message
 
    class Meta:
        ordering = ('timestamp',)


class photos(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, default=None, related_name="attachments")
    images = models.ImageField(blank=True, upload_to='pictures')