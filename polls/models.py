from __future__ import absolute_import

from django.db import models
from django_extensions.db.models import TimeStampedModel

from accounts.models import User
from venues.models import Venue


class Question(TimeStampedModel):
    user = models.ForeignKey(User)
    completed = models.BooleanField(default=False)


class Answer(TimeStampedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User)

    def __str__(self):
        return "Answer object: %d" % (self.id)


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
        return "VenueRating object: %d" % (self.id)
