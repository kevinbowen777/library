import uuid
from datetime import date

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the book's language")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    pages = models.IntegerField(blank=True, help_text="Number of Pages")
    publisher = models.CharField(max_length=40, blank=True)
    pubdate = models.DateField(null=True, blank=True, help_text="Date Published")
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book.")
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        unique=True,
        help_text="13 Character <a href='https://www.isbn-international.org/content/what-isbn'>ISBN number</a>",
    )
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["title", "author"]

    def display_genre(self):
        """Creates a string for Genre. Required for Admin display"""
        return ", ".join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = "Genre"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])


class BookInstance(models.Model):
    """Represents a specific copy of a book"""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text="Unique ID for this book across whole library"
    )
    book = models.ForeignKey("Book", on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On Loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="m",
        help_text="Book Availability",
    )

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return f"{self.id} ({self.book.title})"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True, help_text="Middle Name(initial)")
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("Died", null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])

    def __str__(self):
        if self.middle_name is not None:
            return f"{self.last_name}, {self.first_name} {self.middle_name}"
        else:
            return f"{self.last_name}, {self.first_name}"
