from django.contrib import admin
from .models import Message, ChatThread
# Register your models here.

admin.site.register(ChatThread)
admin.site.register(Message)

