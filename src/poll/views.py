from django.shortcuts import render, redirect
from .models import Polls

def current(request):
    objects = Polls.objects.order_by('id')

    data = {
        'type': 'last',
        'polls': objects[len(objects) - 1:]
    }
    return render(request, 'poll/current.html', data)
