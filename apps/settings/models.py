from django.db import models

# Create your models here.

class Settings(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип',
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название сайта',
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта',
    )
    description = models.TextField(
        verbose_name='Описание сайта',
    )
 
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Настройки сайта'


class Advantage(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название преимущества',
    )
    description = models.TextField(
        verbose_name='Описание преимущества',
    )
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'


class Service(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название услуги',
    )
    description = models.TextField(
        verbose_name='Описание услуги',
    )
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Наши услуги'

class Our_team(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя преподавателя',
    )
    position = models.CharField(
        max_length=255,
        verbose_name='Должность преподавателя',
    )
    photo = models.ImageField(
        upload_to='team/',
        verbose_name='Фотография преподавателя',
    )
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Наша команда'




class About_us(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок  о нас',
    )
    description = models.TextField(
        verbose_name='Описаниео нас',
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta: 
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class About_advantage(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название преимущества',
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества в разделе о нас'

class Review(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя',
    )
    work = models.CharField(
        max_length=255,
        verbose_name='Место работы',
    )
    review = models.TextField(
        verbose_name='Отзыв',
    )
    photo = models.ImageField(
        upload_to='reviews/',
        verbose_name='Фотография',
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок новости',
    )
    description = models.TextField(
        verbose_name='Описание новости',
    )
    photo = models.ImageField(
        upload_to='news/',
        verbose_name='Фотография',
    )
    date = models.DateField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Contact(models.Model):
    email = models.CharField(
        max_length=255,
        verbose_name='Почта',
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес',
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон',
    )

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = 'Контактная информация'

class Information(models.Model):
    lesson_count = models.IntegerField(
        verbose_name='Количество  проведенных уроков',
    )
    student_count = models.IntegerField(
        verbose_name='Количество студентов',
    )
    course = models.IntegerField(
        verbose_name='Количество курсов',
    )
    awards = models.IntegerField(
        verbose_name='Количество наград',
    )

    def __str__(self) -> str:
        return 'Информация о нашем учебном центре'
    
    class Meta:
        verbose_name = 'Информация о нашем учебном центре'
        verbose_name_plural = 'Информация о нашем учебном центре'