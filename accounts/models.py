from __future__ import absolute_import

from django.db import models
from django_extensions.db.models import TimeStampedModel

from authtools.models import AbstractEmailUser


class User(AbstractEmailUser):
    name = models.CharField('name', max_length=255, blank=True)
    picture = models.ImageField('picture', blank=True)

    def get_name(self):
        return self.name

    def get_picture(self):
        return self.picture

    def __str__(self):
        return '{name} <{email}>'.format(
            name=self.name,
            email=self.email,
        )


class Group(TimeStampedModel):
    name = models.CharField('name', max_length=255)
    members = models.ManyToManyField(User, through='Membership')

    def __str__(self):
        return self.name


class Membership(TimeStampedModel):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    leader = models.BooleanField(default=False)

    def __str__(self):
        return '{user_name} <{group_name}>'.format(
            user_name=self.user,
            group_name=self.group
        )