from django import forms
from finalboss.models import User, Reksadana

class userForm(forms.ModelForm):
    fullName = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = User
        fields = ('fullName','address')

class reksaDanaForm(forms.ModelForm):
    name = forms.CharField()
    unitPrice = forms.CharField()
    unitNumber = forms.IntegerField()
    class Meta:
        model = Reksadana
        fields = '__all__'