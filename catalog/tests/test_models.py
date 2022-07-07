from django.test import TestCase

from ..models import Author, Genre


class GenreModelTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name="Fiction")

    def test_genre___str__(self):
        assert self.genre.__str__() == self.genre.name
        assert str(self.genre) == self.genre.name


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        Author.objects.create(first_name="Thomas", last_name="Pynchon")
        Author.objects.create(
            first_name="William",
            last_name="Burroughs",
            middle_name="S.",
        )

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("first_name").verbose_name
        self.assertEqual(field_label, "first name")

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("last_name").verbose_name
        self.assertEqual(field_label, "last name")

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("date_of_birth").verbose_name
        self.assertEqual(field_label, "date of birth")

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("date_of_death").verbose_name
        self.assertEqual(field_label, "Died")

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field("first_name").max_length
        self.assertEqual(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field("last_name").max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = "{0}, {1}".format(
            author.last_name, author.first_name
        )

        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), "/catalog/author/1")

    def test_middlename__str__(self):
        author = Author.objects.get(id=2)
        if author.middle_name is not None:
            self.assertEqual(
                author.__str__(),
                f"{author.last_name}, {author.first_name} {author.middle_name}",
            )
        else:
            self.assertEqual(
                author.__str__(), f"{author.last_name}, {author.first_name}"
            )
