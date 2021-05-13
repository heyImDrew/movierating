from django.test import TestCase

from films.models import Film


class TestCases(TestCase):
    def setUp(self):
        Film.objects.create()