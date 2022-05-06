from django.contrib import admin

from .models import Author, Book, BookInstance, Genre, Language

admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)


class BooksInline(admin.TabularInline):
    """Defines format of inline book insertions"""

    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """

    list_display = ("last_name", "first_name", "middle_name", "date_of_birth", "date_of_death")
    fields = ["first_name", "middle_name", "last_name", ("date_of_birth", "date_of_death")]
    inlines = [BooksInline]
