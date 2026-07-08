from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from nubel_project.translations import tr
from .models import CustomUser

INPUT = "form-input"


def _username_label(lang):
    return "Имя пользователя" if lang.startswith("ru") else "Foydalanuvchi nomi"


def _password_label(lang):
    return "Пароль" if lang.startswith("ru") else "Parol"


def _password2_label(lang):
    return "Повторите пароль" if lang.startswith("ru") else "Parolni takrorlang"


class RegisterForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": INPUT, "placeholder": "+998 __ ___ __ __"
        }),
    )

    class Meta:
        model = CustomUser
        fields = ("username", "phone_number", "password1", "password2")
        widgets = {"username": forms.TextInput(attrs={"class": INPUT})}

    def __init__(self, *args, lang="uz", **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = _username_label(lang)
        self.fields["phone_number"].label = tr("f.phone", lang)
        self.fields["password1"].label = _password_label(lang)
        self.fields["password2"].label = _password2_label(lang)
        self.fields["password1"].widget.attrs.update({"class": INPUT})
        self.fields["password2"].widget.attrs.update({"class": INPUT})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, lang="uz", **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = _username_label(lang)
        self.fields["password"].label = _password_label(lang)
        self.fields["username"].widget.attrs.update({"class": INPUT})
        self.fields["password"].widget.attrs.update({"class": INPUT})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "phone_number", "photo")
        widgets = {
            "first_name": forms.TextInput(attrs={"class": INPUT}),
            "last_name": forms.TextInput(attrs={"class": INPUT}),
            "email": forms.EmailInput(attrs={"class": INPUT}),
            "phone_number": forms.TextInput(attrs={"class": INPUT}),
        }

    def __init__(self, *args, lang="uz", **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].label = tr("f.first", lang)
        self.fields["last_name"].label = tr("f.last", lang)
        self.fields["email"].label = tr("f.email", lang)
        self.fields["phone_number"].label = tr("f.phone", lang)
        self.fields["photo"].label = tr("prof.photo", lang)
