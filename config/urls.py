from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # User management
    path("accounts/", include("django.contrib.auth.urls")),
    # Application specific
    path("catalog/", include("catalog.urls")),
    path("", RedirectView.as_view(url="catalog/", permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
