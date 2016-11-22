from django.contrib import admin

from .models import *


class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified',)
    list_display = ('id', 'user', 'completed', 'created', 'modified',)


class AnswerAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified',)
    list_display = ('id', 'question', 'user', 'created', 'modified',)


class QuestionVenueAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified',)
    list_display = ('id', 'question', 'venue', 'created', 'modified',)


class VenueRatingAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified',)
    list_display = ('id', 'answer', 'question_venue', 'rating', 'created', 'modified',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(QuestionVenue, QuestionVenueAdmin)
admin.site.register(VenueRating, VenueRatingAdmin)
