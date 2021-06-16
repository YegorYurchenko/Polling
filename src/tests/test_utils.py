""" Модуль тестирования вспомогательных функций """

from django.test import TestCase
from poll.templatetags.poll_split import split, split_space_for_result
from poll.views import add_answer_increase
from create_poll.views import delete_empty_variants

class UtilsTest(TestCase):
    """ Тестирование вспомогательных функций (utils) """

    def test_split_valid(self):
        """ Тестирование функии разбиения по символу переносу строки """
        self.assertEqual(split('МГУ\nВШЭ\nМГТУ\nМФТИ\nМГИМО'),
                        ['МГУ', 'ВШЭ', 'МГТУ', 'МФТИ', 'МГИМО'])

    def test_split_space_for_result_valid(self):
        """ Тестирование функции преобразования результата голосования в проценты """
        self.assertEqual(split_space_for_result('2 5 1 3 9'),
                        ['10.0%', '25.0%', '5.0%', '15.0%', '45.0%'])

    def test_add_answer_increase_valid(self):
        """ Тестирование функции увеличения количества голосов """
        self.assertEqual(add_answer_increase('2 5 1 3 9', 2), '2 5 2 3 9')

    def test_delete_empty_variants(self):
        """ Тестирование функции, удаляющей пустые варианты голосования """
        self.assertEqual(delete_empty_variants('МГУ\nВШЭ\n\n\nМГТУ\n\n МФТИ\nМГИМО\n\n'),
                        'МГУ\nВШЭ\nМГТУ\nМФТИ\nМГИМО')
