from django import forms
from crimeReporting.models import *

class UPDATE_FORM(forms.ModelForm):

  class Meta:
    model = CRIME_TIMELINE
    fields = ['CURRENT_STATUS', 'TIME_OF_UPDATE', 'DESCRIPTION']
    widgets = {
        'DESCRIPTION': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
    }






