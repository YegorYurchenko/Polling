""" Модуль тестирования отображения  """

from django.test import TestCase
from django.urls import reverse
from poll.models import Polls

class AuthorListViewTest(TestCase):
    """ Тестирование отображения страниц """

    @classmethod
    def setUpTestData(cls):
        """ Создание объекта голосования """
        Polls.objects.create(title='Лучший ВУЗ Москвы?',
                            variants='МГУ\nВШЭ\nМГТУ\nМФТИ\nМГИМО',
                            answers='2 5 1 3 9')


    # Страница "Текущее голосование"
    def test_view_url_exists_at_desired_location_current(self):
        """ Проверка URL-адреса по пути """
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_current(self):
        """ Проверка URL-адреса по имени """
        resp = self.client.get(reverse('current'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_current(self):
        """ Проверка правильности использования шаблона """
        resp = self.client.get(reverse('current'))
        self.assertTemplateUsed(resp, 'poll/current.html')


    # Страница "Все голосования"
    def test_view_url_exists_at_desired_location_all_polls(self):
        """ Проверка URL-адреса по пути """
        resp = self.client.get('/all_polls/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_all_polls(self):
        """ Проверка URL-адреса по имени """
        resp = self.client.get(reverse('all_polls'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_all_polls(self):
        """ Проверка правильности использования шаблона """
        resp = self.client.get(reverse('all_polls'))
        self.assertTemplateUsed(resp, 'all_polls/all_polls.html')


    # Страница "Голосовать в определённом голосовании"
    def test_view_url_exists_at_desired_location_all_polls_id(self):
        """ Проверка URL-адреса по пути """
        resp = self.client.get('/all_polls/1')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_all_polls_id(self):
        """ Проверка URL-адреса по имени """
        resp = self.client.get(reverse('selected_poll', args='1'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_all_polls_id(self):
        """ Проверка правильности использования шаблона """
        resp = self.client.get(reverse('selected_poll', args='1'))
        self.assertTemplateUsed(resp, 'poll/current.html')


    # Страница "Результаты выбранного голосования"
    def test_view_url_exists_at_desired_location_all_polls_result_id(self):
        """ Проверка URL-адреса по пути """
        resp = self.client.get('/all_polls/result_1')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_all_polls_result_id(self):
        """ Проверка URL-адреса по имени """
        resp = self.client.get(reverse('poll_result', args='1'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_all_polls_result_id(self):
        """ Проверка правильности использования шаблона """
        resp = self.client.get(reverse('poll_result', args='1'))
        self.assertTemplateUsed(resp, 'all_polls/poll_result.html')


    # Страница "Новое голосование"
    def test_view_url_exists_at_desired_location_create_poll(self):
        """ Проверка URL-адреса по пути """
        resp = self.client.get('/create_poll')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_create_poll(self):
        """ Проверка URL-адреса по имени """
        resp = self.client.get(reverse('create_poll'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_create_poll(self):
        """ Проверка правильности использования шаблона """
        resp = self.client.get(reverse('create_poll'))
        self.assertTemplateUsed(resp, 'create_poll/create_poll.html')
