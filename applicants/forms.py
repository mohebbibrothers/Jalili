from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'last_name', 'national_code', 'phone_number','type' , 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control shadow-lg rounded', 'placeholder': 'نام'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control shadow-lg rounded', 'placeholder': 'نام خانوادگی'}),
            'national_code': forms.TextInput(attrs={'class': 'form-control shadow-lg rounded', 'placeholder': 'کد ملی'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control shadow-lg rounded', 'placeholder': 'شماره تلفن'}),
            'type': forms.Select(attrs={'class': 'form-select shadow-lg rounded'}),
            'location': forms.TextInput(attrs={'class': 'form-control shadow-lg rounded', 'placeholder': 'مکان'}),
        }