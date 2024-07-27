from django.db import models

class Telegram2(models.Model):
    fullname = models.CharField(
        max_length=255,
        verbose_name='Имя',
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Email',
    )
    message = models.TextField(
        verbose_name='Сообщение',
    )

    def __str__(self) -> str:
        return self.fullname

    class Meta:
        verbose_name = 'Заявка на Telegram2'
        verbose_name_plural = 'Заявки на Telegram2'

