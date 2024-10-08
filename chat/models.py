from django.db import models
from django.contrib.auth import get_user_model


class Message(models.Model):
    sender = models.ForeignKey(
        get_user_model(), related_name='messages', verbose_name='Отправитель', on_delete=models.SET_NULL, null=True,
        blank=True)

    text = models.TextField('Текст')

    class Meta:
        db_table = 'Message'
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.id
