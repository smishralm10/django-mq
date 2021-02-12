from django import forms

class Quantity(forms.Form):
    quantity = forms.IntegerField(label='How much data do you want?', required=True)
    
