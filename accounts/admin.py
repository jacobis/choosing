from django.contrib import admin

from .models import *


class AccountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'date_joined',)


class GroupsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified',)
    list_display = ('id', 'name', 'created', 'modified',)


class MembershipAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified',)
    list_display = ('id', 'group', 'user', 'leader', 'created', 'modified',)


admin.site.register(User, AccountsAdmin)
admin.site.register(Group, GroupsAdmin)
admin.site.register(Membership, MembershipAdmin)