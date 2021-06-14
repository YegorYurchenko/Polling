from django.shortcuts import render

def current(request):
    return render(request, 'poll/current.html')
