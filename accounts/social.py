from django.core.files.base import ContentFile

from social.utils import slugify
from urllib.request import urlopen


def create_user(strategy, details, user=None, *args, **kwargs):
    if user: return {'is_new': False}

    fields = {'email': details.get('email'), 'name': details.get('fullname')}
    return {
        'is_new': True,
        'user': strategy.create_user(**fields)
    }

def save_profile_picture(strategy, user, response, details, *args, **kwargs):
    url = 'http://graph.facebook.com/{0}/picture?type=large'.format(response['id'])
    picture = urlopen(url)
    user.picture.save(slugify('{0}_social'.format(user.email)) + '.jpg', ContentFile(picture.read()))
    user.save()
