from django.db import models

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
