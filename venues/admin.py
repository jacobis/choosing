from django.contrib import admin

from .models import Venue


class VenueAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified',)
    list_display = ('name', 'address', 'created', 'modified',)

admin.site.register(Venue, VenueAdmin)