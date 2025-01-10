from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields =  ['student_number', 'first_name', 'last_name', 'subject','grade_year', 'grade']
        labels = {
            'student_number': 'Student Number', 
            'first_name': 'First Name', 
            'last_name': 'Last Name', 
            'subject': 'Subject',
            'grade_year': 'Grade Year',
            'grade': 'Grade'
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'grade_year': forms.TextInput(attrs={'class': 'form-control'}), 
            'grade': forms.NumberInput(attrs={'class': 'form-control'})
}

