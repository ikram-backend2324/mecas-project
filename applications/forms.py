from django import forms
from nubel_project.translations import tr
from .models import Application, Programme, Faculty

INPUT = "form-input"
FILE = "file-input"


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = (
            "programme", "faculty",
            "first_name", "last_name", "middle_name",
            "date_of_birth", "passport_number",
            "phone_number", "email",
            "passport_file", "diploma_transcript",
            "school_certificate", "photo", "certificate",
        )
        widgets = {
            "programme": forms.Select(attrs={"class": INPUT}),
            "faculty": forms.Select(attrs={"class": INPUT}),
            "first_name": forms.TextInput(attrs={"class": INPUT}),
            "last_name": forms.TextInput(attrs={"class": INPUT}),
            "middle_name": forms.TextInput(attrs={"class": INPUT}),
            "date_of_birth": forms.DateInput(
                attrs={"class": INPUT, "type": "date"}),
            "passport_number": forms.TextInput(
                attrs={"class": INPUT, "placeholder": "AA1234567"}),
            "phone_number": forms.TextInput(
                attrs={"class": INPUT, "placeholder": "+998 __ ___ __ __"}),
            "email": forms.EmailInput(attrs={"class": INPUT}),
            "passport_file": forms.ClearableFileInput(attrs={"class": FILE}),
            "diploma_transcript": forms.ClearableFileInput(attrs={"class": FILE}),
            "school_certificate": forms.ClearableFileInput(attrs={"class": FILE}),
            "photo": forms.ClearableFileInput(attrs={"class": FILE}),
            "certificate": forms.ClearableFileInput(attrs={"class": FILE}),
        }

    def __init__(self, *args, lang="uz", **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["programme"].queryset = Programme.objects.filter(
            is_active=True)
        self.fields["faculty"].queryset = Faculty.objects.filter(
            is_active=True)
        placeholder = tr("select.placeholder", lang)
        self.fields["programme"].empty_label = placeholder
        self.fields["faculty"].empty_label = placeholder
        # Optional documents
        self.fields["diploma_transcript"].required = False
        self.fields["certificate"].required = False
