from django import forms


class CustomForm(forms.Form):
    company_name = forms.CharField(max_length=255)
    position = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    description = forms.CharField(max_length=10000)
    category = forms.CharField(max_length=255)


