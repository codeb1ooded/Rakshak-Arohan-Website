from django import forms
from prediction.models import RScript

class RScriptForm(forms.ModelForm):
    class Meta:
        model = RScript
        fields = '__all__'
        print("" + fields)

        def __init__(self):
            self.fields['script'].label = "script"

