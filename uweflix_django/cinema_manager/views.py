from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Film, Club, Screen, Showing #This is the structure if you want to import a class from models.py.
from django.urls import reverse
from django.template import loader

# Create your views here.

def hello(request):
    return HttpResponse('Hello') 

def add_film(request):
    if 'title' in request.GET and request.GET['title']:
        c1 = request.GET['title']
    if 'rating' in request.GET and request.GET['rating']:
        c2 = request.GET['rating']
    if 'duration' in request.GET and request.GET['duration']:
        c3 = request.GET['duration']
    if 'trailer_desc' in request.GET and request.GET['trailer_desc']:
        c4 = request.GET['trailer_desc']
    film = Film(title=c1, age_rating=c2, duration=c3, trailer_description=c4)
    film.save()
    return HttpResponse("Success!")      
    #pass

def delete_film(request, id):
    film = Film.objects.get(id=id)
    film.delete()
    return HttpResponse("Delete Success!") 

def display_film(request):
    films_qs = Film.objects.all().values()
    template = loader.get_template('films.html')
    context = {
        'films': films_qs,
    }
    print('Test')
    return HttpResponse(template.render(context, request))

    
#The system will handle the table of club details and film details in a similar way.
#Only the data will be different.
def add_club(request):
    if 'name' in request.GET and request.GET['name']:
        c1 = request.GET['name']
    if 'address' in request.GET and request.GET['address']:
        c2 = request.GET['address']
    if 'contacts' in request.GET and request.GET['contacts']:
        c3 = request.GET['contacts']
    if 'representative' in request.GET and request.GET['representative']:
        c4 = request.GET['representative']
    club = Club(name=c1, address=c2, contacts=c3, representative=c4)
    club.save()
    return HttpResponse("Success!")      
    #pass

def delete_club(request, id):
    club = Club.objects.get(id=id)
    club.delete()
    return HttpResponse("Delete Success!") 

def display_club(request):
    clubs_qs = Club.objects.all().values()
    template = loader.get_template('clubs.html')
    context = {
        'clubs': clubs_qs,
    }
    return HttpResponse(template.render(context, request))

def add_screen(request):
    if 'capacity' in request.GET and request.GET['capacity']:
        c1 = request.GET['capacity']
    if 'seat_number' in request.GET and request.GET['seat_number']:
        c2 = request.GET['seat_number']
    if 'social_dist' in request.GET and request.GET['social_dist']:
        c3 = request.GET['social_dist']
    screen= Screen(capacity=c1, seat_number=c2, social_dist=c3)
    screen.save()
    return HttpResponse("Success!")      
    #pass

def delete_screen(request, id):
    screen = Screen.objects.get(id=id)
    screen.delete()
    return HttpResponse("Delete Success!") 

def display_screen(request):
    screen_qs = Screen.objects.all().values()
    template = loader.get_template('screens.html')
    context = {
        'screens': screen_qs,
    }
    return HttpResponse(template.render(context, request))

def add_showing(request):
    if 'title' in request.GET and request.GET['title']:
        c1 = request.GET['title']
    if 'date' in request.GET and request.GET['date']:
        c2 = request.GET['date']
    if 'time' in request.GET and request.GET['time']:
        c3 = request.GET['time']
    showing= Showing(title=c1, date=c2, time=c3)
    showing.save()
    return HttpResponse("Success!")      
    #pass

def delete_showing(request, id):
    showing = Showing.objects.get(id=id)
    showing.delete()
    return HttpResponse("Delete Success!") 

def display_showing(request):
    showing_qs = Showing.objects.all().values()
    template = loader.get_template('showings.html')
    context = {
        'showings':showing_qs,
    }
    return HttpResponse(template.render(context, request))


    # films = list(films_qs.values())
    # return render(request, "films.html")