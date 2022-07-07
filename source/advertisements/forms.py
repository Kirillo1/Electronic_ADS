from django import forms

from advertisements.models import Advertisement


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ("title", "description", "images", "category", "price")


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")
