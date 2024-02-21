# forms.py

from django import forms
from .models import Document,Contact

class UploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file']
class UploadText(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['text']
    # You can add custom validation or override form methods if necessary
