from django.contrib import admin

from .models import *


class AccountsAdmin(admin.ModelAdmin):
    pass


class GroupsAdmin(admin.ModelAdmin):
    pass


class MembershipAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, AccountsAdmin)
admin.site.register(Group, GroupsAdmin)
admin.site.register(Membership, MembershipAdmin)