# TODO: Implement Routings Here
from django.urls import path
from katalog.views import show_items

app_name = 'katalog'

urlpatterns = [
    path('', show_items, name='show_items'),
]