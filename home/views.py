from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Team

def home(request):
    team = Team.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'team': team,
    }
    return HttpResponse(template.render(context, request))

