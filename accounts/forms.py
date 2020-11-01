from django.contrib.auth import get_user_model
from django import forms

non_allowed_usernames = ['abc']
# check for unique email and username

User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=True)
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'user-password'
            }
        )
    )
    password2 = forms.CharField(
        label='Confirmation Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'user-confirm-password'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if username in non_allowed_usernames:
            raise forms.ValidationError("Invalid user name. Please use another one.")
        if qs.exists():
            raise forms.ValidationError("Invalid user name. Please use another one.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'user-password'
            }
        )
    )

    # def clean(self):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Invalid user.")
        return username
