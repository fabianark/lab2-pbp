from django.shortcuts import render
from mywatchlist.models import MyWatchlistItem
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.

def show_watchlist(request):
    return render(request, 'mywatchlist_home.html')

def show_watchlist_html(request):
    data = MyWatchlistItem.objects.all()
    watched = 0
    not_watched = 0
    text_response = ""

    # Bonus
    for item in data.values():
        if (item.get("watched") == True):
            watched += 1
        else:
            not_watched += 1
    
    if watched >= not_watched:
        text_response = "Selamat, kamu sudah banyak menonton!"
    else:
        text_response = "Wah, kamu masih sedikit menonton!"

    context = {
        'watchlist': data,
        'text_response': text_response
    }
    return render(request, 'mywatchlist.html', context)

def show_watchlist_xml(request):
    data = MyWatchlistItem.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_watchlist_json(request):
    data = MyWatchlistItem.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")