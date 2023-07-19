from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    """фaрма"""
    class Meta:
        model = ContactModel
        fields = '__all__'

