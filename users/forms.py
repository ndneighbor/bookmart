import re
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile, User


class LogoutForm(forms.Form):
    pass


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance')
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    def validate_non_numeric(self, str_exp):
        pattern = re.compile(r"([a-zA-Z]+)")
        if not pattern.match(str_exp):
            raise ValidationError('Field is incorrect')
        return str_exp

    def clean_first_name(self):
        return self.validate_non_numeric(self.cleaned_data['first_name'])

    def clean_last_name(self):
        return self.validate_non_numeric(self.cleaned_data['last_name'])

    def clean_email(self):
        value = self.cleaned_data['email']
        pattern = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if not pattern.match(value):
            raise ValidationError('Email format is incorrect')
        return value


"""
    def clean(self):
        super(UserProfileForm, self).clean()
        self.first_name = self.cleaned_data.get('first_name')
        self.last_name = self.cleaned_data.get('last_name')
        self.email = self.cleaned_data.get('email')
        self.username = self.cleaned_data.get('user')
"""


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nick_name']

    def clean_nick_name(self):
        value = self.cleaned_data['email']
        pattern = re.compile(r"(^[a-zA-Z]+[a-zA-Z0-9-]+$)")
        if not pattern.match(value):
            raise ValidationError('Email format is incorrect')
        return value


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields