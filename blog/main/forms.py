from django import forms
from .models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class' : 'common-input mb-20 form-control',
            'placeholder': 'Your Name',
            'onblur' : 'this.placeholder',
            'onfocus' : 'this.placeholder'
        }
    ))

    email = forms.EmailField(required=False, widget=forms.EmailInput(
        attrs={
            'class' : 'common-input mb-20 form-control',
            'placeholder': 'Your Email',
            'onblur' : 'this.placeholder',
            'onfocus' : 'this.placeholder'
        }
    ))

    text = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'mb-10 form-control',
            'placeholder': 'Type Comment...',
            'onblur' : 'this.placeholder',
            'onfocus' : 'this.placeholder'
        }
    ))


class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'contact_input contact_input_name',
            'placeholder': 'Your Name'
        }
    ))

    email = forms.EmailField(required=False, widget=forms.EmailInput(
        attrs={
            'class': 'contact_input contact_input_email',
            'placeholder': 'Your Email'
        }
    ))

    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'contact_text',
            'placeholder': 'Type Message...'
        }
    ))
