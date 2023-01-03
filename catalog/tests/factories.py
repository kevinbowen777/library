import datetime

import factory
import factory.fuzzy
import pytest

from ..models import Author, Book, Genre


@pytest.fixture
def author():
    return AuthorFactory()


@pytest.fixture
def genre():
    return GenreFactory()


@pytest.fixture
def book():
    return BookFactory()


class AuthorFactory(factory.django.DjangoModelFactory):
    first_name = factory.fuzzy.FuzzyText(length=12)
    middle_name = factory.fuzzy.FuzzyText(length=5)
    last_name = factory.fuzzy.FuzzyText(length=10)
    date_of_birth = factory.fuzzy.FuzzyDate(
        datetime.date(1860, 3, 20),
        datetime.date(1920, 3, 20),
    )
    date_of_death = factory.fuzzy.FuzzyDate(
        datetime.date(1930, 3, 20),
        datetime.date(2021, 3, 20),
    )

    class Meta:
        model = Author


class GenreFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText(length=12)

    class Meta:
        model = Genre


class BookFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=12, prefix="The Book of ")
    author = factory.SubFactory(AuthorFactory)
    genre = factory.RelatedFactory(
        GenreFactory,
        # factory_related_name='genre',
    )
    # genre = factory.fuzzy.FuzzyText(length=10)
    pages = factory.fuzzy.FuzzyInteger(low=1, high=399)
    publisher = factory.fuzzy.FuzzyText(length=12, prefix="The Book of ")
    pubdate = factory.fuzzy.FuzzyDate(
        datetime.date(1960, 3, 20),
        datetime.date(2021, 3, 20),
    )

    class Meta:
        model = Book

    @factory.post_generation
    def genre(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of genres were passed in, use them
            for genre in extracted:
                self.genre.add(genre)
