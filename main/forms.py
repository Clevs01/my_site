# from django import forms
# class ContactForm(forms.Form):
#     first = forms.CharField(label='Your first name', max_length=100)
#     last = forms.CharField(label='Your last name', max_length=100)
#     email = forms.EmailField(label='Your email', max_length=100)
#     country = forms.CharField(label='Your country', max_length=100)
#     address = forms.CharField(label='Your name', max_length=100)
#     your_name = forms.CharField(label='Your name', max_length=100)
from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('title', 'name', 'email', 'country', 'address', 'phone', 'message')
