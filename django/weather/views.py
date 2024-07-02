from django.shortcuts import render
from .models import Forecast

def home(request):
    messages = Forecast.objects.all()
    return render(request, "home.html", { "messages": messages })
