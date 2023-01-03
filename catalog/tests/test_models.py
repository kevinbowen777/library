from django.test import TestCase

from .factories import AuthorFactory, BookFactory
from ..models import Genre, Language


class BookModelTest(TestCase):
    def setUp(self):
        # Create a book
        self.author = AuthorFactory()
        self.book = BookFactory()

    def test_book___str__(self):
        assert self.book.__str__() == self.book.title
        assert str(self.book) == self.book.title

    def test_get_absolute_url(self):
        url = self.book.get_absolute_url()
        assert url == f"/catalog/book/{self.book.id}"


class GenreModelTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name="Fiction")

    def test_genre___str__(self):
        assert self.genre.__str__() == self.genre.name
        assert str(self.genre) == self.genre.name


class LanguageModelTest(TestCase):
    def setUp(self):
        self.language = Language.objects.create(name="English")

    def test_genre___str__(self):
        assert self.language.__str__() == self.language.name
        assert str(self.language) == self.language.name


class AuthorModelTest(TestCase):
    """Set up non-modified objects used by all test methods."""

    def setUp(self):
        self.author = AuthorFactory()
        """
        @classmethod
        def setUpTestData(cls):
        Author.objects.create(first_name="Thomas", last_name="Pynchon")
        Author.objects.create(
            first_name="William",
            last_name="Burroughs",
            middle_name="S.",
        )
        """

    def test_first_name_label(self):
        field_label = self.author._meta.get_field("first_name").verbose_name
        self.assertEqual(field_label, "first name")

    def test_last_name_label(self):
        field_label = self.author._meta.get_field("last_name").verbose_name
        self.assertEqual(field_label, "last name")

    def test_date_of_birth_label(self):
        field_label = self.author._meta.get_field("date_of_birth").verbose_name
        self.assertEqual(field_label, "date of birth")

    def test_date_of_death_label(self):
        field_label = self.author._meta.get_field("date_of_death").verbose_name
        self.assertEqual(field_label, "Died")

    def test_first_name_max_length(self):
        max_length = self.author._meta.get_field("first_name").max_length
        self.assertEqual(max_length, 100)

    def test_last_name_max_length(self):
        max_length = self.author._meta.get_field("last_name").max_length
        self.assertEqual(max_length, 100)

    """
    def test_object_name_is_last_name_comma_first_name(self):
        # author = Author.objects.get(id=1)
        expected_object_name = "{0}, {1}".format(
            self.author.last_name, self.author.first_name
        )

        self.assertEqual(str(self.author), expected_object_name)
    """

    def test_get_absolute_url(self):
        self.assertEqual(
            self.author.get_absolute_url(), f"/catalog/author/{self.author.id}"
        )

    def test_middlename__str__(self):
        if self.author.middle_name is not None:
            self.assertEqual(
                self.author.__str__(),
                f"{self.author.last_name}, {self.author.first_name} {self.author.middle_name}",  # noqa:B950
            )
        else:
            self.assertEqual(
                self.author.__str__(),
                f"{self.author.last_name}, {self.author.first_name}",
            )
