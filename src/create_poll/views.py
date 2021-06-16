""" Create_poll views """

from django.shortcuts import render, redirect
from .forms import PollsForm

def createPoll(request): # Не create_poll из-за условия задачи
    """ Создание нового голосования """

    error = ''
    if request.method == 'POST':
        form = PollsForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.variants = delete_empty_variants(poll.variants)

            amount_of_variants = len(poll.variants.split('\n'))
            poll.answers = ' '.join(['0' for i in range(amount_of_variants)]) # никто не голосовал
            poll.save()
            return redirect('current')

        error = 'Вы неправильно заполнили форму'

    form = PollsForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'create_poll/create_poll.html', data)

def delete_empty_variants(variants: str) -> str:
    """ Функция, удаляющая пустые варианты голосования """
    new_variants = variants.split('\n')

    result_variants = []
    for variant in new_variants:
        if len(variant.strip()) > 0:
            result_variants.append(variant.strip())

    return '\n'.join(result_variants)
