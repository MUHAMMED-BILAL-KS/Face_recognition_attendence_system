from django import forms
from . models import *

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'
class student_form(forms.ModelForm):
    class Meta:
        model = student
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','id':'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','id':'last_name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','id':'phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control','id':'email'}),
            'dob': DateInput(attrs={'class': 'form-control','id':'dob'}),           #for date input i made above
            'dept': forms.TextInput(attrs={'class': 'form-control','id':'dept'}),
            'rollno': forms.TextInput(attrs={'class': 'form-control','id':'rollno'}),
            'collage': forms.TextInput(attrs={'class': 'form-control','id':'collage'}),
            'district': forms.TextInput(attrs={'class': 'form-control','id':'district'}),
            'image': forms.FileInput(attrs={'class': 'form-control m-1','type':'file','id':'image'}),
        }
        
        