from django.contrib import admin

from .models import *


class VenueRatingAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified',)
    list_display = ('answer', 'question_venue', 'rating', 'created', 'modified',)

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionVenue)
admin.site.register(VenueRating, VenueRatingAdmin)
