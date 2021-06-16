from django.shortcuts import render, redirect
from poll.models import Polls
from .forms import PollsForm

def createPoll(request):
    error = ''
    if request.method == 'POST':
        form = PollsForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.variants = delete_empty_variants(poll.variants)

            amount_of_variants = len(poll.variants.split('\n'))
            poll.answers = ' '.join(['0' for i in range(amount_of_variants)]) # Пока что никто не проголосовал
            poll.save()
            return redirect('current')
        else:
            error = 'Вы неправильно заполнили форму'

    form = PollsForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'create_poll/create_poll.html', data)

def delete_empty_variants(variants: str) -> str:
    new_variants = variants.split('\n');

    result_variants = []
    for variant in new_variants:
        if len(variant.strip()) > 0:
            result_variants.append(variant.strip())

    return '\n'.join(result_variants)

