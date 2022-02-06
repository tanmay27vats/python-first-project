from django.forms import ModelForm, Textarea, TextInput, EmailInput
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        # fields = '__all__'
        fields = ('full_name', 'email', 'message')
        widgets = {
            'full_name': TextInput(attrs={'max_length': 100, 'class': 'form-control', 'required': 'true', 'placeholder': "Tanmay Vats"}),
            'email': EmailInput(attrs={'max_length': 100, 'class': 'form-control', 'required': 'true', 'placeholder': "name@example.com",
                                   'pattern': "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"}),
            'message': Textarea(attrs={'cols': 80, 'rows': 5, 'class': 'form-control', 'required': 'true'})
        }