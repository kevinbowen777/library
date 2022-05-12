import datetime

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import BookInstance


class RenewBookModelForm(ModelForm):
    def clean_renewal_date(self):
        data = self.cleaned_data["due_back"]

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError("Invalid date - renewal in past")

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError("Invalid date - renewal more than 4 weeks ahead")

        # Remember to always return the cleaned data.
        return data

    class Meta:
        model = BookInstance
        fields = ["due_back"]
        labels = {"due_back": "Renewal date"}
        help_texts = {"due_back": "Enter a date between now and 4 weeks (default 3)."}
