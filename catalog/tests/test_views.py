from django.test import TestCase
from django.urls import reverse

from catalog.models import Author


class AuthorListViewTest(TestCase):
    def setUp(self):
        url = reverse("authors")
        self.response = self.client.get(url)

    @classmethod
    def setUpTestData(cls):
        # Create authors for pagination tests
        number_of_authors = 13
        for author_id in range(number_of_authors):
            Author.objects.create(first_name="Django {0}".format(author_id), last_name="Wilkins {0}".format(author_id))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/catalog/authors/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "catalog/author_list.html")

    def test_pagination_is_ten(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTrue("is_paginated" in self.response.context)
        self.assertTrue(self.response.context["is_paginated"] is True)
        self.assertEqual(len(self.response.context["author_list"]), 10)

    def test_lists_all_authors(self):
        # Get second page and confirm it has (exactly) the remaining 3 items
        response = self.client.get(reverse("authors") + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["author_list"]), 3)
