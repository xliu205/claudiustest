from django import forms
from .models import Accident


class LawsuitForm(forms.ModelForm):
    
    class Meta:
        model = Accident
        fields = [
            'name',
            'gender', 
            'description',
            'annual_wage',
            'medical_expenses',
            'accident_date'
        ]
