from django.contrib import admin

# Register your models here.
from .models import Chatbot

class ChatbotAdmin(admin.ModelAdmin):
    list_display = ['question', 'response', 'created_at', 'updated_at']

admin.site.register(Chatbot, ChatbotAdmin)

