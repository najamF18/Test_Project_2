from django.contrib import admin
from .models import Message, ChatThread, photos
# Register your models here.

admin.site.register(ChatThread)
admin.site.register(Message)
admin.site.register(photos)

