from django.contrib import admin
from .models import Group, Message

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Group, GroupAdmin)
admin.site.register(Message)

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class CustomUserAdmin(BaseUserAdmin):
    actions = ['delete_selected']

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
