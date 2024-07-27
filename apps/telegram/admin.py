
from django.contrib import admin
from apps.telegram.models import Telegram2
# Register your models here.

@admin.register(Telegram2)
class TelegramAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname'] 