from django.db import models

# Create your models here.
class Telegram(models.Model):
    fullname = models.CharField(
        max_length=255,
        verbose_name='ФИО',
    )
    course = models.CharField(
        max_length=255,
        verbose_name='Название Курса',
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон',
    )
    email = models.CharField(
        max_length=255,
        verbose_name='Email',
    )
    def __str__(self) -> str:
       return self.fullname
    
    class Meta:
        verbose_name = 'Заявка на Telegram'
        verbose_name_plural = 'Заявки на Telegram'

