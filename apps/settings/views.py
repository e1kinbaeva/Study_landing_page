from django.http import HttpRequest
from django.shortcuts import render, redirect

from apps.contact.models import Telegram
from apps.contact.views import get_text
from .models import *

def index(request: HttpRequest):
    settings = Settings.objects.latest('id')
    advantage = Advantage.objects.all().order_by('?')[:3]
    service = Service.objects.all().order_by('?')[:6]
    team = Our_team.objects.all().order_by('?')[:4]
    about_us = About_us.objects.latest('id')
    about_advantage = About_advantage.objects.all()
    review = Review.objects.all()
    news = News.objects.all().order_by('-id')[:3]
    contact = Contact.objects.latest('id')
    info = Information.objects.latest('id')

    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        message = request.POST.get('message')
        Telegram.objects.create(fullname=fullname, email=email, message=message )
        get_text(f"""Оставлена заявка 💬:
                 
ФИО: {fullname}

Почта: {email}

Сообщение: {message}

""")
        return redirect('index')
    
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
    return render(request, 'index.html', locals())
