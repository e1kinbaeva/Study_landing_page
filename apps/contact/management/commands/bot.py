from django.core.management.base import BaseCommand
from apps.contact.views import bot

class Command(BaseCommand):
    help = "Bot"

    def handle(self, *args, **kwargs):
        print("START TELEGRAM BOT")
        bot.polling(non_stop=True, interval=0)