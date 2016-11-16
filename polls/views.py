from django.db.models import Avg
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from authtools.models import User
from venues.models import Venue

from .models import Question, Answer, QuestionVenue, VenueRating


def index(request):
    question_list = Question.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'question_list': question_list,
    }

    return HttpResponse(template.render(context, request))

def create(request):
    if request.method == 'GET':
        template = loader.get_template('polls/create.html')
        context = {
            'test': 'test'
        }

        return HttpResponse(template.render(context, request))
    else:
        host = request.user
        users = request.POST.get('users')
        area = request.POST.get('area')
        category = request.POST.get('category')

        question = Question.objects.create(user=host)
        Answer.objects.bulk_create([Answer(question=question, user=User.objects.get(id=user)) for user in users])

        venues = Venue.objects.filter(address__contains=area)[:5]
        QuestionVenue.objects.bulk_create([QuestionVenue(question=question, venue=venue) for venue in venues])

        return HttpResponseRedirect(reverse('polls:index'))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        question_venues = []

        for question_venue in question.questionvenue_set.all():
            question_venues.append({
                'venue': question_venue.venue,
                'rating': question_venue.venuerating_set.all().aggregate(Avg('rating'))['rating__avg']})

    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/results.html', {'question': question, 'question_venues': question_venues})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        answer = Answer.objects.get(question=question)
        question_venues = [QuestionVenue.objects.get(id=question_venue) for question_venue in request.POST.getlist('question_venues')]
        question_venues_with_rank = dict(zip(question_venues, request.POST.getlist('ranks')))

        VenueRating.objects.bulk_create([
            VenueRating(answer=answer, question_venue=qvwr[0], rating=qvwr[1]) for qvwr in question_venues_with_rank.items()
        ])

    except Exception(e):
        print ("vote error: " + e)

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
