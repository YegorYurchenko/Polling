from poll.models import Polls
from django.forms import ModelForm, TextInput, Textarea

class PollsForm(ModelForm):
    class Meta:
        model = Polls
        fields = ['title', 'variants']

        widgets = {
            'title': TextInput(attrs={
                'class': 'poll__create-title js-form-create-title',
                'placeholder': 'Название статьи',
                'autocomplete' : 'off',
                'required': True
            }),
            'variants': Textarea(attrs={
                'class': 'poll__create-variants js-form-create-variants',
                'placeholder': 'Вариант №1\nВариант №2\nВариант №3\n...',
                'cols': 49,
                'required': True
            })
        }
