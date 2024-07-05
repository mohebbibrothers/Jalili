from django import forms
from .models import Provider, Area

class ProviderForm(forms.ModelForm):
    areas = forms.ModelMultipleChoiceField(queryset=Area.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Provider
        fields = ['name', 'last_name', 'national_code', 'phone_number', 'car_name', 'car_color', 'car_tag', 'areas']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control shadow-lg rounded', 'placeholder': 'نام'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control shadow-lg rounded', 'placeholder': 'نام خانوادگی'}),
            'national_code': forms.TextInput(attrs={'class': 'form-control shadow-lg rounded', 'placeholder': 'کد ملی'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control shadow-lg rounded', 'placeholder': 'شماره تلفن'}),
            'car_name': forms.TextInput(attrs={'class': 'form-control shadow-lg rounded', 'placeholder': 'نام خودرو'}),
            'car_color': forms.TextInput(attrs={'class': 'form-control shadow-lg rounded', 'placeholder': 'رنگ خودرو'}),
            'car_tag': forms.TextInput(attrs={'class': 'form-control shadow-lg rounded', 'placeholder': 'پلاک خودرو'}),
        }