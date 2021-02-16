from django.shortcuts import render
from django.http import HttpResponse
from .models import Songs, Users, Concerts
from django.template import loader
from django.http import JsonResponse
from django.db.models import Count
from django.db.models import Avg, Max, Min

# Create your views here.

def index(request):
    songs = Songs.objects.all()
    context = {
        'songs': songs,
    }
    return render(request, 'songs/index.html',context)


def capacity_chart(request):
    labels = []
    data = []

    queryset = Concerts.objects.all().order_by('-date')

    for entry in queryset:
        labels.append(entry.title)
        data.append(entry.date)
    print(data.append(entry.date))
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def stat2(request):
    labels = []
    data = []

    queryset = Songs.objects.values('genre').annotate(gcount=Count('genre'))
    for song in queryset:
        labels.append(song['genre'])
        data.append(song['gcount'])

    return render(request, 'stat2.html', {
        'labels': labels,
        'data': data,
    })

def agregacija(request):
    concerts = Concerts.objects.all()
    listSong = []
    prosek = Concerts.objects.all().aggregate(Avg('date'))
    LjudiMax = Concerts.objects.all().aggregate(Max('date'))
    LjudiMin = Concerts.objects.all().aggregate(Min('date'))
    filterLjudi = Concerts.objects.all().filter(date__gte = 25000)
    print(prosek)
    listSong.append('Prosek publike po koncertima je: ' + str(prosek['date__avg']))
    listSong.append('Max publike po koncertima je: ' + str(LjudiMax['date__max']))
    listSong.append('Min publike po koncertima je: ' + str(LjudiMin['date__min']))
    listSong.append('Vise od 25 000 ljudi imaju koncerti: ')
    for ljudi in filterLjudi:
        listSong.append(ljudi.title + ' ')

    context = {
        'concerts': listSong,
    }

    return render(request, 'songs/agregacija.html',context)

def stat1(request):
    print('CAO')
    return render(request, 'songs/stat1.html')


def stat3(request):
    labels = []
    data = []

    queryset = Concerts.objects.all().order_by('-date')
    for concert in queryset:
        labels.append(concert.title)
        data.append(concert.date)

    return render(request, 'stat3.html', {
        'labels': labels,
        'data': data,
    })