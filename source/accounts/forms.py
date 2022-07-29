from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import BaseModelForm

from accounts.models import Profile


class UserFormValidationMixin(BaseModelForm):
    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if not first_name and not last_name:
            raise forms.ValidationError('Хотя бы одно из полей "Имя" или "Фамилия" должны быть заполнены')
        return super().clean()


class MyUserCreationForm(UserCreationForm, UserFormValidationMixin):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ["username", "password1", "password2", "email", "first_name", "last_name"]
