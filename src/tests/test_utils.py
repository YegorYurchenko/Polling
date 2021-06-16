from django.test import TestCase
from poll.templatetags.poll_split import split, split_space_for_result
from poll.views import add_answer_increase

class PollsFormTest(TestCase):
    """ Тестирование вспомогательных функций """
    
    def test_split_valid(self):
        self.assertEqual(split('МГУ\nВШЭ\nМГТУ\nМФТИ\nМГИМО'), ['МГУ', 'ВШЭ', 'МГТУ', 'МФТИ', 'МГИМО'])

    def test_split_space_for_result_valid(self):
        self.assertEqual(split_space_for_result('2 5 1 3 9'), ['10.0%', '25.0%', '5.0%', '15.0%', '45.0%'])

    def test_add_answer_increase_valid(self):
        self.assertEqual(add_answer_increase('2 5 1 3 9', 2), '2 5 2 3 9')
