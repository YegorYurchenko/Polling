""" Модуль тестирования моделей """

from django.test import TestCase
from poll.models import Polls

class PollsModelTest(TestCase):
    """ Тестирование модели Polls """

    @classmethod
    def setUp(cls):
        """ Создание объекта голосования """
        Polls.objects.create(title='Лучший ВУЗ Москвы?',
                            variants='МГУ\nВШЭ\nМГТУ\nМФТИ\nМГИМО', answers='2 5 1 3 9')

    def test_title_label(self):
        """ Проверка значений текстовых меток (title) """
        poll = Polls.objects.get(id=1)
        field_label = poll._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Название')

    def test_variants_label(self):
        """ Проверка значений текстовых меток (variants) """
        poll = Polls.objects.get(id=1)
        field_label = poll._meta.get_field('variants').verbose_name
        self.assertEquals(field_label,'Варианты')

    def test_answers_label(self):
        """ Проверка значений текстовых меток (answers) """
        poll = Polls.objects.get(id=1)
        field_label = poll._meta.get_field('answers').verbose_name
        self.assertEquals(field_label,'Ответы')

    def test_date_label(self):
        """ Проверка значений текстовых меток (date) """
        poll = Polls.objects.get(id=1)
        field_label = poll._meta.get_field('date').verbose_name
        self.assertEquals(field_label,'Дата публикации')

    def test_title_max_length(self):
        """ Проверка максимальной длины title """
        poll = Polls.objects.get(id=1)
        max_length = poll._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_answers_max_length(self):
        """ Проверка максимальной длины answers """
        poll = Polls.objects.get(id=1)
        max_length = poll._meta.get_field('answers').max_length
        self.assertEquals(max_length, 100)

    def test_poll_str(self):
        """ Проверка метода __str__ """
        poll = Polls.objects.get(id=1)
        self.assertEquals(str(poll), 'Лучший ВУЗ Москвы?')

    def test_object_modification(self):
        """ Проверка возможности изменения данных в БД """
        poll = Polls.objects.get(id=1)
        poll.title = 'Лучший ВУЗ Санкт-Петербурга'
        poll.variants = 'СПбГУ\nСПбПУ\nИТМО\nСПГУ'
        poll.answers = '34 12 53 26'
        poll.save()
        self.failIfEqual(poll.title, 'Лучший ВУЗ Москвы?')
        self.failIfEqual(poll.variants, 'МГУ\nВШЭ\nМГТУ\nМФТИ\nМГИМО')
        self.failIfEqual(poll.answers, '2 5 1 3 9')
