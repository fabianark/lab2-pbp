from multiprocessing.connection import Client
from django.test import TestCase, Client
from django.urls import reverse
from mywatchlist.views import show_watchlist_html, show_watchlist_xml, show_watchlist_json

class Test(TestCase):
    def test_html(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_watchlist_html"))
        assert response.status_code == 200, "FAILED"
        print(f"test html: HTTP {response.status_code} OK")

    
    def test_xml(self):
        client = Client(self)
        response = client.get(reverse("mywatchlist:show_watchlist_xml"))
        assert response.status_code == 200, "FAILED"
        print(f"test xml: HTTP {response.status_code} OK")

    def test_json(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_watchlist_json"))
        assert response.status_code == 200, "FAILED"
        print(f"test json: HTTP {response.status_code} OK")