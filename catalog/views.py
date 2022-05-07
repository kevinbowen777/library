from django.shortcuts import render
from django.views import generic

from .models import Author, Book, BookInstance, Genre  # noqa:F401


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    num_authors = Author.objects.count()
    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
    }

    return render(request, "index.html", context=context)


class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""

    model = Book
    paginate_by = 5


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""

    model = Book


class AuthorListView(generic.ListView):
    """Generic class-based list view for a list of authors."""

    model = Author
    paginate_by = 5


class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""

    model = Author
