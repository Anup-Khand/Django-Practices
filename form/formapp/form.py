from django import forms


class StudentRegistration(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()


class FormRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()