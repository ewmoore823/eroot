from django.shortcuts import render
from django.http import HttpResponse

from main.models import Climb

def main(request):
    return HttpResponse("this is the main page :)")

def climbs(request):
    climbs = Climb.objects.all()

    context = { 'climbs': climbs, }
    return HttpResponse(render(request, 'main/climbs.html', context))

def foundation(request):
    return HttpResponse(render(request, 'main/foundation.html', {}))

# Create your views here.
