from django.shortcuts import render
from django.conf  import settings
from telebot import TeleBot, types
from apps.telegram.models import Telegram2
# Create your views here.


# Create your views here.
TELEGRAM_TOKEN = "7050472655:AAH2mWGYbzY_SI1C9SRQknFTelK_Tc7JY3w"
ADMIN_ID = 766589023

bot = TeleBot(TELEGRAM_TOKEN, threaded=False)
admin_id = ADMIN_ID

@bot.message_handler(commands=['start'])
def start(message:types.Message):
    Telegram2.objects.get_or_create(username = message.from_user.username, id_user=message.from_user.id, first_name = message.from_user.first_name, last_name = message.from_user.last_name,)
    # bot.delete_message(message.chat.id, message.message_id) 
    bot.send_message(message.chat.id, f"Привет {message.from_user.full_name}")

class Mail:
    def __init__(self): 
        self.description = None

mail = Mail()


def get_message(message:types.Message):
    mail.description = message.text 
    users = Telegram2.objects.all()
    for user in users:
        bot.send_message(user.id_user, mail.description)
    bot.send_message(message.chat.id, "Рассылка окончена")

@bot.message_handler(commands=['mailing'])
def send_mailing(message:types.Message):
    if message.chat.id != int(admin_id):
        bot.send_message(message.chat.id, "Эта команда доступна только админу")
        return
    msg = bot.send_message(message.chat.id, "Введите текст для рассылки: ")
    bot.register_next_step_handler(msg, get_message)

def get_text(message):
    bot.send_message(admin_id, message)

def get_text_doctor(message, id):
    bot.send_message(id, message)


@bot.message_handler()  
def echo(message:types.Message):
    # bot.delete_message(message.chat.id, message.message_id)  
    bot.send_message(message.chat.id, "Я вас не понял")