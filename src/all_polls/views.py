from django.shortcuts import render, redirect
from poll.models import Polls
from django.views.generic import DetailView

def all_polls(request):
    objects = Polls.objects.order_by('-id')

    data = {
        'type': 'all',
        'polls': objects
    }
    return render(request, 'all_polls/all_polls.html', data)


class PollDetailView(DetailView):
    model = Polls
    template_name = 'poll/current.html'
    context_object_name = 'poll'

class getResult(DetailView):
    model = Polls
    template_name = 'all_polls/poll_result.html'
    context_object_name = 'poll'
