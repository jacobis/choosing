from django.shortcuts import get_object_or_404, render

from .models import Venue


def index(request):
    venue_list = Venue.objects.all().order_by('-modified')
    context = {'venue_list': venue_list}

    return render(request, 'venues/index.html', context)


def detail(request, venue_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    
    return render(request, 'venues/detail.html', {'venue': venue})