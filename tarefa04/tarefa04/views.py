from django.shortcuts import render

from .models import Missão
from datetime import date

def index(request):
    context = {
        'missoes': Missão.objects.all(),
        'hoje': date.today(),
    }

    return render(request, 'index.html', context)