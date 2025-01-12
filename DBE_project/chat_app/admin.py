from django.contrib import admin
from .models import Group, Friend, Message, Emoji


# Register your models here.

admin.site.register(Group)
admin.site.register(Friend)
admin.site.register(Message)
admin.site.register(Emoji)