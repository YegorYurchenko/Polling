""" Poll views """

from django.shortcuts import render, redirect
from .models import Polls


def poll(request):
    """ Голосование в конкретном опросе """

    if request.method == 'POST':
        poll_id = request.POST.get("poll_id")
        answer_idx = request.POST.get("common_radio")

        if (poll_id and answer_idx):
            poll_item = Polls.objects.get(pk=poll_id)
            poll_item.answers = add_answer_increase(poll_item.answers, int(answer_idx))
            poll_item.save()

            return redirect('all_polls')

    objects = Polls.objects.order_by('id')

    data = {
        'type': 'last'
    }

    if len(objects) > 0:
        data['polls'] = objects[len(objects) - 1:]
    else:
        data['polls'] = None
    return render(request, 'poll/current.html', data)

def add_answer_increase(results: str, idx: int) -> str:
    """ Функция увеличения количества голосов """
    new_results = list(map(int, results.split()))
    new_results[idx] += 1
    new_results = list(map(str, new_results))
    return ' '.join(new_results)
