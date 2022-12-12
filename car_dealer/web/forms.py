from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from car_dealer.web.models import Listing, Feedback, ContactForm, Comment


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': ' form-control',
                'placeholder': 'Username..',
            }),
            'email': forms.EmailInput(attrs={
                'class': ' form-control',
                'placeholder': 'Email..',
            }),
            'first_name': forms.TextInput(attrs={
                'class': ' form-control',
                'placeholder': 'First name..',
            }),
            'last_name': forms.TextInput(attrs={
                'class': ' form-control',
                'placeholder': 'Last name..',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': ' form-control', 'placeholder': 'Enter password..'})
        self.fields['password2'].widget = forms.PasswordInput(
                attrs={'class': ' form-control', 'placeholder': 'Re-enter Password...'})


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['brand', 'model', 'price', 'description', 'image','year','engine','color']

    def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        self.fields['brand'].widget = forms.TextInput(attrs={'placeholder': 'Brand..'})
        self.fields['model'].widget = forms.TextInput(attrs={'placeholder': 'Model..'})
        self.fields['price'].widget = forms.NumberInput(attrs={'placeholder': 'Price..'})
        self.fields['year'].widget = forms.NumberInput(attrs={'placeholder': 'Production year..'})
        self.fields['engine'].widget = forms.TextInput(attrs={'placeholder': 'Engine..'})
        self.fields['color'].widget = forms.TextInput(attrs={'placeholder': 'Color..'})
        self.fields['description'].widget = forms.Textarea(attrs={'placeholder': 'Enter description..'})


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.Textarea(attrs={'placeholder': 'Comment..'})
        self.fields['full_name'].widget.attrs['readonly'] = True



class TicketForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'First name..', 'class': 'form-control'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Last name..', 'class': 'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Email..', 'class': 'form-control'})
        self.fields['phone_number'].widget = forms.NumberInput(attrs={'placeholder': 'Phone number..', 'class': 'form-control'})
        self.fields['message'].widget = forms.Textarea(attrs={'placeholder': 'Your Message..', 'class': 'form-control'})


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.Textarea(attrs={'placeholder': 'Comment..'})

