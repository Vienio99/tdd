from django.test import TestCase
from django.urls import resolve
from lists.views import home

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/home/')
        self.assertEqual(found.func, home)