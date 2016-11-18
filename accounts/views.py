from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from .models import *


@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required()
def index_group(request):
    context = {}
    template = loader.get_template('groups/index.html')
    memberships = Membership.objects.filter(user=request.user, leader=True)

    group_list = []
    for membership in memberships:
        group_list.append(Membership.objects.filter(group=membership.group))

    context.update({'group_list': group_list})

    return HttpResponse(template.render(context, request))


@login_required
def create_group(request):
    if request.method == 'GET':
        template = loader.get_template('groups/create.html')
        context = {}

        return HttpResponse(template.render(context, request))

    else:
        leader = request.user
        name = request.POST.get('name')
        members = request.POST.get('members').split(',')

        group = Group.objects.create(name=name)
        Membership.objects.create(user=leader, group=group, leader=True)
        Membership.objects.bulk_create([Membership(user=User.objects.get(id=member), group=group)
                                        for member in members])

        return HttpResponseRedirect(reverse('home'))


@login_required
def detail_group(request, group_id):
    try:
        group = Group.objects.get(pk=group_id)

    except Group.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'groups/detail.html', {'group': group})

