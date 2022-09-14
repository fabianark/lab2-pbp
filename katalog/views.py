from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

def show_items(request):
    response = {
        'list_item': CatalogItem.objects.all(),
        'name': "Fabian Akmal Arkandion",
        'npm': "2106750660"
    }
    return render(request, 'katalog.html', response)