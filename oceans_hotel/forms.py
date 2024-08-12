from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'



class SignUpForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'input-field', 'type':'password', 'placeholder':'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'input-field', 'type':'password', 'placeholder':'Retype Password'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class':'input-field', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Email', 'required': 'true'}),
            'first_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'First Name', 'required': 'true'}),
            'last_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Last Name', 'required': 'true'})
        }

class BookRoomForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["check_in"].widget.attrs['data-validation'] = "check-in-validation"
        self.fields["check_in"].widget.attrs['readonly'] = True
        self.fields["check_in"].widget.attrs['class'] = "prevent-change"

        self.fields["check_out"].widget.attrs['data-validation'] = "check-out-validation"
        self.fields["check_out"].widget.attrs['readonly'] = True
        self.fields["check_out"].widget.attrs['class'] = "prevent-change"

        self.fields["total_cost"].widget.attrs['readonly'] = True
        self.fields["total_cost"].widget.attrs['class'] = "prevent-change"

    class Meta:
        model= Bookings
        fields = ['check_in', 'check_out', 'total_cost']
        widgets = {
            'check_in': DateInput(),
            'check_out': DateInput(),
        }
