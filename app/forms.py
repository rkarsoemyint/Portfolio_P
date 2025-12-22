from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'သင့်အမည်'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'အီးမေးလ်'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'အကြောင်းအရာ'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'စာသားများ...', 'rows': 4}),
        }