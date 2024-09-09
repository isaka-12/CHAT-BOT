from django.shortcuts import render
from django.views.generic import ListView

from landingPage.models import Chatbot

# Create your views here.

class ChatbotView(ListView):
    model = Chatbot
    template_name = 'index.html'
    context_object_name = 'chatbot'
    
    def get_queryset(self):
        return Chatbot.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chatbot'] = Chatbot.objects.all()
        return context
   