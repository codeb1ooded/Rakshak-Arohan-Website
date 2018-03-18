from django.contrib.auth.models import User
from django import forms
from .models import FIR_REPORT

class FirRegistrationForm(forms.ModelForm):
    class Meta:
        model = FIR_REPORT
        fields = '__all__'
        exclude = ('LAT', 'LNG','FIR_LOC')

        widgets = {
            'CRIME_DESCRIPTION': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
            'DATE_CRIME': forms.DateInput(attrs={'class':'datepicker'}),
        }

        print (""+fields)
    # print("jaclin")

    #def __init__(self):
    #self.fields['first_name'].label = "First Name"
class UserRegistrationForm(forms.Form):
    name = forms.CharField(
        required = True,
        label = 'NAME',
        max_length = 100
    )
    username = forms.CharField(
        required = True,
        label = 'USERNAME',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'EMAIL',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'PASSWORD',
        max_length = 32,
        widget = forms.PasswordInput()
    )


class UserAuthenticationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'USERNAME',
        max_length = 32
    )
    password = forms.CharField(
        required = True,
        label = 'PASSWORD',
        max_length = 32,
        widget = forms.PasswordInput()
    )
