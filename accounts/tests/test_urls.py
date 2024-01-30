import pytest
from django.urls import resolve, reverse

from ..models import CustomUser

pytestmark = pytest.mark.django_db


def test_detail(user: CustomUser):
    assert (
        reverse("user_detail", kwargs={"username": user.username})
        == f"/accounts/{user.username}/"
    )
    assert resolve(f"/accounts/{user.username}/").view_name == "user_detail"


def test_update():
    assert reverse("user_update") == "/accounts/~update/"
    assert resolve("/accounts/~update/").view_name == "user_update"


def test_redirect():
    assert reverse("redirect") == "/accounts/~redirect/"
    assert resolve("/accounts/~redirect/").view_name == "redirect"
