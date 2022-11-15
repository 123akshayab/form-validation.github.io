from django import forms
from django.core.exceptions import ValidationError
from core.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"
        

    def clean(self):
        """
        Raise `ValidationError` if user didn't provide both name and email.
        """
        cleaned_data = super().clean() 
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")

        if not name and not email:
            raise ValidationError("Please provide name or email.")
        
        return cleaned_data

