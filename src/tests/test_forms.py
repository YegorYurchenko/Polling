""" Модуль тестирования форм """

from django.test import TestCase
from create_poll.forms import PollsForm

class PollsFormTest(TestCase):
    """ Тестирование формы PollsForm """

    def test_poll_title_form_field_label(self):
        """ Проверка текста поля title """
        form = PollsForm()
        self.assertTrue(form.fields['title'].label is None or
            form.fields['title'].label == 'Название')

    def test_poll_variants_form_field_label(self):
        """ Проверка текста поля variants """
        form = PollsForm()
        self.assertTrue(form.fields['variants'].label is None or
            form.fields['variants'].label == 'Варианты')

    def test_poll_good_data(self):
        """ Проверка валидности (good) """
        form_data = {'title': 'Лучший ВУЗ Москвы?', 'variants': 'МГУ\nВШЭ\nМГТУ\nМФТИ\nМГИМО'}
        form = PollsForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_poll_bad_title(self):
        """ Проверка валидности (bad title) """
        form_data = {'title': '', 'variants': 'МГУ\nВШЭ\nМГТУ\nМФТИ\nМГИМО'}
        form = PollsForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_poll_bad_variants(self):
        """ Проверка валидности (bad variants) """
        form_data = {'title': 'Лучший ВУЗ Москвы?', 'variants': ''}
        form = PollsForm(data=form_data)
        self.assertFalse(form.is_valid())
