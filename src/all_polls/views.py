""" All_polls views """

from django.shortcuts import render
from django.views.generic import DetailView
from poll.models import Polls

def all_polls(request):
    """ Показ всех голований """
    objects = Polls.objects.order_by('-id')

    data = {
        'type': 'all',
        'polls': objects
    }
    return render(request, 'all_polls/all_polls.html', data)


class PollDetailView(DetailView):
    """ Страница 'Голосовать' выбранного голосования """
    model = Polls
    template_name = 'poll/current.html'
    context_object_name = 'poll'

class GetResult(DetailView):
    """ Страница 'Результат' выбранного голосования """
    model = Polls
    template_name = 'all_polls/poll_result.html'
    context_object_name = 'poll'
