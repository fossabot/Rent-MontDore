from django.contrib import admin

# Register your models here.

from contact.models import Message

admin.site.register(Message)
