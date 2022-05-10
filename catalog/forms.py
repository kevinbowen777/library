import datetime  # noqa:F401

from django import forms
from django.core.exceptions import ValidationError  # noqa:F401
from django.utils.translation import gettext_lazy as _  # noqa:F401


class RenewBookForm(forms.Form):
    """Form for a librarian to renew books."""

    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data["renewal_date"]

        # Check date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_("Invalid date - renewal in past"))
