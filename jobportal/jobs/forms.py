from django import forms
from .models import JobApplication

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'cover_letter']