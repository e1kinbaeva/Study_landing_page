from django.core.mail import send_mail
from django.http import HttpRequest
from django.shortcuts import render, redirect
from apps.contact.models import Telegram
from apps.contact.views import get_text
from .models import Settings, Advantage, Service, Our_team, About_us, About_advantage, Review, News, Contact, Information, Smtp

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
        form_type = request.POST.get("form_type")
        if form_type == "contact_form":
            name = request.POST.get("fullname")
            email = request.POST.get("email_smtp")
            message = request.POST.get('message')
            Smtp.objects.create(name=name, email=email, message=message)
            send_mail(
                subject=f'New Contact Form Submission from {name} email - {email}',
                message=message,
                from_email=email,
                recipient_list=['ainazikerkinbaeva2106200414@gmail.com'],
            )
        elif form_type == "callback_form":
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

""")  # Send message via Telegram
        return redirect('index')

    return render(request, 'index.html', locals())
