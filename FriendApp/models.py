from django.db import models
from LoginApp.models import User

# Create your models here.

class FriendList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    friends = models.ManyToManyField(User, blank=True)

class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receive")