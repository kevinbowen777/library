import datetime  # noqa:F401

from django import forms
from django.core.exceptions import ValidationError  # noqa:F401
from django.utils.translation import gettext_lazy as _  # noqa:F401


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
