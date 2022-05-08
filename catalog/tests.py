from django.test import TestCase
from django.urls import reverse


class HomepageTests(TestCase):
    def test_index_status_code(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 301)

    def test_index_url_name(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")
