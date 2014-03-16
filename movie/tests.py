from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http.request import HttpRequest
from django.template.loader import render_to_string

from .views import home_page
from .models import Movie

class HomePageTest(TestCase):

    def test_home_page_url_resolve(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_html_content(self):
        request = HttpRequest()
        request.method = 'GET'
        response = home_page(request)
        expected_html = render_to_string("home.html")
        self.assertEqual(response.content, expected_html)


class MovieModelTest(TestCase):

    def test_movie_get_request_not_save_content(self):
        request = HttpRequest()
        request.method = 'GET'
        home_page(request)
        self.assertEqual(Movie.objects.count(), 0)

    def test_save_and_retrieve_movies(self):
        movie_troy       = "Frozon"
        movie_terminator = "Terminator"

        Movie.objects.create(name = movie_troy)
        Movie.objects.create(name = movie_terminator)

        movies = Movie.objects.all()

        self.assertEqual(movies.count(), 2)

        self.assertEqual(movie_troy,       movies[0].name)
        self.assertEqual(movie_terminator, movies[1].name)


    def test_no_save_and_retrieve_movies(self):
        Movie.objects.create(name = "Frozon")
        Movie.objects.create(name = "Terminator")

        request = HttpRequest()
        request.method = 'GET'
        response = home_page(request)

        self.assertIn("Frozon", response.content)
        self.assertIn("Terminator", response.content)
