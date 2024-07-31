from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.password_validation import validate_password

class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True,
        "class": "form-control",
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            "class": "form-control",
        }),
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="user name",
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder" : "This field must be unique",
        }),
    )
    first_name = forms.CharField(
        label="First name",
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
        }),
    )
    last_name = forms.CharField(
        label="Last name",
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
        }),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
        }),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
        }),
    )
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
        }),
    )

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        
        if validate_password(password ,user=None,password_validators=None) != None:
            raise forms.ValidationError
