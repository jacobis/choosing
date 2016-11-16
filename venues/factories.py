import factory
from .models import Venue


class VenueFactory(factory.Factory):
    class Meta:
        model = Venue

    name = '누하의 숲'
    address = '	종로구 옥인3길 5-1, 서울특별시'
