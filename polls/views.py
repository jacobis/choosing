from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from accounts.models import User
from venues.models import Venue

from .models import Question, Answer, QuestionVenue, VenueRating


@login_required
def home(request):
    context = {}
    template = loader.get_template('polls/home.html')

    if request.user.is_authenticated():
        current_question_list = Question.current.all().filter(answer__user=request.user)
        past_question_list = Question.past.all().filter(answer__user=request.user)

        context.update({'current_question_list': current_question_list, 'past_question_list': past_question_list})

    return HttpResponse(template.render(context, request))


@login_required
def create(request):
    if request.method == 'GET':
        template = loader.get_template('polls/create.html')
        context = {}

        return HttpResponse(template.render(context, request))

    else:
        host = request.user
        users = request.POST.get('users').split(',')
        area = request.POST.get('area')
        category = request.POST.get('category')

        question = Question.objects.create(user=host)
        Answer.objects.bulk_create([Answer(question=question, user=User.objects.get(id=user)) for user in users])

        venues = Venue.objects.filter(address__contains=area)[:5]
        QuestionVenue.objects.bulk_create([QuestionVenue(question=question, venue=venue) for venue in venues])

        return HttpResponseRedirect(reverse('home'))


@login_required
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)

    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', {'question': question})


@login_required
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


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        answer = Answer.objects.get(question=question, user=request.user)
        question_venues = [QuestionVenue.objects.get(id=question_venue) for question_venue in
                           request.POST.getlist('question_venues')]
        question_venues_with_rank = dict(zip(question_venues, request.POST.getlist('ranks')))

        VenueRating.objects.bulk_create([VenueRating(answer=answer, question_venue=qvwr[0], rating=qvwr[1])
                                         for qvwr in question_venues_with_rank.items()])

    except Exception as e:
        print("vote error: " + e)

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
