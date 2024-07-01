from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email')
    number = forms.CharField(label='Your phone number', max_length=15)
    message = forms.CharField(widget=forms.Textarea)