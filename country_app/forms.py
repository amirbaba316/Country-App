from django import forms

class NameForm(forms.Form):
    Country = forms.CharField(widget=forms.TextInput(attrs={
        'style': 'border-color:SteelBlue; border-radius: 7px; border-width: thin;',
        }))