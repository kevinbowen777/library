"""URLs for the library  project."""
from django.conf import settings  # noqa:F401
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django admin
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("resources/", admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # Local apps
    path("accounts/", include("accounts.urls")),
    path("", include("pages.urls")),
    path("catalog/", include("catalog.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
if settings.DEBUG:
    import debug_toolbar  # noqa: F401  # pragma: no cover

    urlpatterns = [  # pragma: no cover
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
"""
