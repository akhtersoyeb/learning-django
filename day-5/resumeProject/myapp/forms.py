from django import forms 
from .models import Resume 

GENDER_CHOICES = [
    ('Male', 'Male'), 
    ('Female', 'Female'), 
    ('Others', 'Others')
]

class ResumeForm(forms.ModelForm): 
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    class Meta: 
        model = Resume 
        fields = ['name', 'dob', 'gender', 'locality', 'state', 
                    'profile_image', 'doc_file']
        labels = {'name': 'name', 
                    'dob': 'date of birth', 
                    'profile_image': 'Profile Image', 
                    'doc_file': 'Extra Documents'}

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}), 
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}), 

        }