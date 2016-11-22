from __future__ import absolute_import

from django.db import models
from django.db.models import Avg
from django_extensions.db.models import TimeStampedModel

from datetime import datetime

from accounts.models import User
from venues.models import Venue


class CurrentManager(models.Manager):
    def get_queryset(self):
        return super(CurrentManager, self).get_queryset().filter(created__date=datetime.today())


class PastManager(models.Manager):
    def get_queryset(self):
        return super(PastManager, self).get_queryset().filter(created__date__lt=datetime.today())


class Question(TimeStampedModel):
    objects = models.Manager()
    current = CurrentManager()
    past = PastManager()

    user = models.ForeignKey(User)
    completed = models.BooleanField(default=False)

    def get_question_venues(self):
        question_venues = []
        for question_venue in self.questionvenue_set.all():
            question_venues.append({
                'venue': question_venue.venue,
                'rating': question_venue.venuerating_set.all().aggregate(Avg('rating'))['rating__avg']})

        return question_venues

    question_venues = property(get_question_venues)

    def __str__(self):
        return "Question object: %d" % self.id


class Answer(TimeStampedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User)

    def __str__(self):
        return "Answer object: %d" % self.id


class QuestionVenue(TimeStampedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue)

    def __str__(self):
        return self.venue.name


class VenueRating(TimeStampedModel):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    question_venue = models.ForeignKey(QuestionVenue, on_delete=models.CASCADE)
    rating = models.FloatField()

    def __str__(self):
        return "VenueRating object: %d" % self.id