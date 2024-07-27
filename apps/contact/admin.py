from django.contrib import admin
from apps.contact.models import Telegram
# Register your models here.

@admin.register(Telegram)
class TelegramAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'phone']
    
# admin.site.register(Telegram)  