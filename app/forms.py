from django import forms
from app.forms import Customer

class customerForm(forms.ModelForm):
    name = forms.CharField()
    age = forms.IntegerField()
    dateOfBirth = forms.DateField(widget=forms.SelectDateWidget)
    accountNumber = forms.CharField(max_length=50)
    phoneNumber = forms.CharField(max_length=50)
    address = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Customer
        fields = '__all__'