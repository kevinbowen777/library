from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Author, Book, BookInstance, Genre  # noqa:F401


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    num_authors = Author.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_visits": num_visits,
    }

    return render(request, "index.html", context=context)


class BookListView(LoginRequiredMixin, ListView):
    """Generic class-based view for a list of books."""

    model = Book
    paginate_by = 10


class BookDetailView(LoginRequiredMixin, DetailView):
    """Generic class-based detail view for a book."""

    model = Book


class AuthorListView(LoginRequiredMixin, ListView):
    """Generic class-based list view for a list of authors."""

    model = Author
    paginate_by = 10


class AuthorDetailView(LoginRequiredMixin, DetailView):
    """Generic class-based detail view for an author."""

    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = "catalog/bookinstance_list_borrowed_user.html"
    paginate_by = 2

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact="o").order_by("due_back")


class LoanedBooksAllListView(PermissionRequiredMixin, ListView):
    model = BookInstance
    permission_required = "catalog.can_mark_returned"
    template_name = "catalog/bookinstance_list_borrowed_all.html"
    paginate_by = 2

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact="o").order_by("due_back")
