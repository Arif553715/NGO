from django import forms
from .models import Contact_list

class CreateForms(forms.ModelForm):
    class Meta:
        model=Contact_list
        fields=[
            'name',
            'mail',
            'message',
        ]