from django import forms
from guest_book.models import GuestBook


class GuestBookForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = ["name", "email", "text"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "email": forms.TextInput(attrs={"placeholder": "Email Address"}),
        }


class SearchForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = ["name"]
        widgets = {"name": forms.TextInput(attrs={"placeholder": "Enter name"})}
