from django import forms
from .models import Credit

class Credit_Form(forms.ModelForm):
    class Meta:
        model = Credit 
        fields = ('name', 'major','number','year','grade','credit', ) 
