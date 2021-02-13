from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm

from .models import ShopUser
from string import ascii_letters


class ShopUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = ShopUser
        fields = ("username", "password")


class ShopUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    def clean_age(self):
        data = self.cleaned_data["age"]
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data

    def clean_first_name(self):
        data = self.cleaned_data["first_name"]
        for c in data:
            if c not in ascii_letters:
                raise forms.ValidationError("Введите латинскими буквами")
        return data

    class Meta:
        model = ShopUser
        fields = ("username", "first_name", "password1", "password2", "email", "age", "avatar")


class ShopUserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    def clean_age(self):
        data = self.cleaned_data["age"]
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data

    def clean_first_name(self):
        data = self.cleaned_data["first_name"]
        for c in data:
            if c not in ascii_letters:
                raise forms.ValidationError("Введите латинскими буквами")
        return data

    class Meta:
        model = ShopUser
        fields = ("username", "first_name", "email", "age", "avatar")