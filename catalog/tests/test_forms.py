import datetime

from django.test import TestCase

from catalog.forms import RenewBookModelForm


class RenewBookModelFormTest(TestCase):
    def test_renew_form_date_in_past(self):
        """Test form is invalid if due_back is before today."""
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = RenewBookModelForm(data={"due_back": date})
        self.assertFalse(form.is_valid())

    def test_renew_form_date_too_far_in_future(self):
        """Test form is invalid if due_back more than 4 weeks from today."""
        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        form = RenewBookModelForm(data={"due_back": date})
        self.assertFalse(form.is_valid())

    def test_renew_form_date_today(self):
        """Test form is valid if due_back is today."""
        date = datetime.date.today()
        form = RenewBookModelForm(data={"due_back": date})
        self.assertTrue(form.is_valid())

    def test_renew_form_date_max(self):
        """Test form is valid if due_back is within 4 weeks."""
        date = datetime.date.today() + datetime.timedelta(weeks=4)
        form = RenewBookModelForm(data={"due_back": date})
        self.assertTrue(form.is_valid())

    def test_renew_form_date_field_label(self):
        """Test due_back label is 'Renewal Date'."""
        form = RenewBookModelForm()
        self.assertTrue(form.fields["due_back"].label is None or form.fields["due_back"].label == "Renewal date")

    def test_renew_form_date_field_help_text(self):
        """Test due_back help_text is as expected."""
        form = RenewBookModelForm()
        self.assertEqual(form.fields["due_back"].help_text, "Enter a date between now and 4 weeks (default 3).")
