from django import forms
from django.core.exceptions import ValidationError
from .models import Item
import string
import re

def name_valid(value):
    if len(value)<3:
        raise ValidationError("must be at least 3")

class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={"placeholder": "Search Items"})
    )

    def clean_search(self):
        search = self.cleaned_data.get("search", "").strip()
        search = search.translate(str.maketrans("", "", string.punctuation))
        if search and len(search) < 3:
            raise ValidationError("Search term must have at least 3 letters.")

        return search

class ItemForm(forms.ModelForm):
    name = forms.CharField(validators=[name_valid])
    class Meta:
        model = Item
        fields = ["name", "description", "category", "brand", "color", "location", "tags"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3, "cols": 40}),
            "tags": forms.CheckboxSelectMultiple(),
        }
        labels = {
            "name": "Item Name",
            "description": "Full Description",
            "category": "Category",
            "brand": "Brand (optional)",
            "color": "Color (optional)",
            "location": "Location Found",
            "tags": "Tags",
        }

    def clean_color(self):
        color = self.cleaned_data.get("color", "").strip()

        if not re.match(r"^[a-zA-Z]+$", color):
            raise ValidationError("Color must contain only letters.")
