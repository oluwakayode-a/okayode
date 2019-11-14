from django import forms
from .models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'comment_input comment_input_name',
            'placeholder': 'Your Name'
        }
    ))

    email = forms.EmailField(required=False, widget=forms.EmailInput(
        attrs={
            'class': 'comment_input comment_input_email',
            'placeholder': 'Your Email'
        }
    ))

    text = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'comment_text',
            'placeholder': 'Type Comment...'
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
