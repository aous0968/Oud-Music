from django import forms
from .models import Track


class AddTrackForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Track
        fields = ["name" , "track" , "track_img"]

    def __init__(self, *args, **kwargs):
        super(AddTrackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

# class AddTrackForm(forms.Form):
#     name = forms.CharField(
#         label="track name",
#         max_length=255,
#         required=True,
#         widget=forms.TextInput(attrs={
#             "class": "form-control",
#             "placeholder" : "Every track must have a name",
#         }),
#     )
#     track_image = forms.FileField(
        
#     )
#     track = forms.FileField(
        
#     )
    
# username = forms.CharField(
#         label="user name",
#         max_length=150,
#         required=True,
#         widget=forms.TextInput(attrs={
#             "class": "form-control",
#             "placeholder" : "This field must be unique",
#         }),
#     )
#     first_name = forms.CharField(
#         label="First name",
#         max_length=150,
#         required=True,
#         widget=forms.TextInput(attrs={
#             "class": "form-control",
#         }),
#     )
#     last_name = forms.CharField(
#         label="Last name",
#         max_length=150,
#         widget=forms.TextInput(attrs={
#             "class": "form-control",
#         }),
#     )
#     email = forms.EmailField(
#         required=True,
#         widget=forms.EmailInput(attrs={
#             "class": "form-control",
#         }),
#     )
#     password = forms.CharField(
#         required=True,
#         widget=forms.PasswordInput(attrs={
#             "class": "form-control",
#         }),
#     )
#     confirm_password = forms.CharField(
#         required=True,
#         widget=forms.PasswordInput(attrs={
#             "class": "form-control",
#         }),
#     )
