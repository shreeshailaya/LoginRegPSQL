from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Destination
from django.contrib.auth.models import User, auth


def index(request):
    data = Destination.objects.all()

    return render(request, 'index.html', {'data': data})


def data(request):
    if request.user.is_authenticated:
        return render(request, 'data_page.html')
    else:
        return render(request, 'index.html')
