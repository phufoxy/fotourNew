from django.shortcuts import render
from .models import Speak,TaskSpeak

# Create your views here.
def index(request):
    speak = Speak.objects.all()
    context = {
        'speak':speak
    }
    return render(request,'home/learn/learn.html',context)