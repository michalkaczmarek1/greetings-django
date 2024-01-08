from django.test import TestCase
from django.urls import resolve
from greetings.views import greetings, greetings_with_name


class TestUrls(TestCase):
    def test_resolution_for_greetings(self):
        resolver = resolve('/greetings/')
        self.assertEqual(resolver.func, greetings)

    def test_resolution_for_greetings_with_name(self):
        resolver = resolve('/greetings/test')
        self.assertEqual(resolver.func, greetings_with_name)
    