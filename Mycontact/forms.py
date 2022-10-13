from django import forms
from .models import Contact
from django.forms import ModelForm
class contactform2(forms.Form):
    firstname=forms.CharField(max_length=10)
    lastname=forms.CharField(max_length=10)
    Email=forms.EmailField()
    msg=forms.CharField(widget=forms.Textarea)
class contactform3(ModelForm):
    class Meta:
        model=Contact
        fields=('firstname','lastname','Email','message')