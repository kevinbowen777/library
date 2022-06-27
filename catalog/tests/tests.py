from django.test import TestCase
from django.urls import resolve, reverse

from ..views import index


class IndexTests(TestCase):
    def setUp(self):
        url = reverse("index")
        self.response = self.client.get(url)

    def test_index_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_contains_correct_html(self):
        self.assertContains(self.response, "Catalog contents")

    def test_index_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "About Page")

    def test_index_template(self):
        self.assertTemplateUsed(self.response, "index.html")

    def test_index_page_url_resolves_index(self):
        view = resolve("/catalog/")
        self.assertEqual(view.func.__name__, index.__name__)
