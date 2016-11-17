from django.contrib import admin

from .models import *


class AccountsAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, AccountsAdmin)
