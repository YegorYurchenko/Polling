""" Models """

from django.db import models
from django.utils.timezone import now

class Polls(models.Model):
    """ Модель Polls """
    title = models.CharField('Название', max_length=100)
    variants = models.TextField('Варианты')
    answers = models.CharField('Ответы', max_length=100)
    date = models.DateTimeField('Дата публикации', default=now, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'
