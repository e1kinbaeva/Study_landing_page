from django.http import HttpRequest
from django.shortcuts import render, redirect

from apps.contact.models import Telegram
from apps.contact.views import get_text
from .models import Settings, Advantage, Service, Our_team,Smtp, About_us,About_advantage,Review,News

from django.core.mail import send_mail


def create_contact(name,email, message):
    Smtp.objects.create(name=name, email=email,  message=message)

def index(request: HttpRequest):
    settings = Settings.objects.latest('id')
    advantage = Advantage.objects.all().order_by('?')[:3]
    service = Service.objects.all().order_by('?')[:6]
    team = Our_team.objects.all().order_by('?')[:4]
    about_us = About_us.objects.latest('id')
    about_advantage = About_advantage.objects.all()
    review = Review.objects.all()
    news = News.objects.all().order_by('-id')[:3]
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        course = request.POST.get("course")
        phone = request.POST.get('phone')
        email = request.POST.get("email")
        Telegram.objects.create(fullname=fullname, course=course, phone=phone, email=email)
        get_text(f"""Оставлена заявка 💬:
                 
ФИО: {fullname}

Название курса: {course}

Номер телефона: {phone}

Почта: {email}
""")
        return redirect('index')
    # функция для создания записи в модели Contacts


# форма обратного связи

    if request.method == "POST":
        name = request.POST.get('form[nom]')
        email = request.POST.get('form[email]')
        message = request.POST.get('form[message]')

        send_mail(
            'Cheff Contact',
            f"""Здравствуйте.
            Спасибо за обратную связь, мы скоро свами свяжемся.
            Ваше ФИО: {name}
            Ваш email: {email}
            Ваше сообщение: {message}...

            Если вы ошиблись при указании данных можете обратно зайти на сайт и оставить новый отзыв с исправленными
            данными! """,
            "noreply@somehost.local",
            ["ainazikerkinbaeva21@gmail.com"]
        )
        # Создание записи в модели Contactsё
        create_contact(name, email, message)

        return redirect('index')
    return render(request, 'index.html', locals())
