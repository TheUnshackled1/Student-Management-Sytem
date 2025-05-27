from django import forms
from .models import Student
from django.core.exceptions import ValidationError 



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'subject', 'grade_year', 'grade']
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
    
    def clean_student_number(self):
        student_number = self.cleaned_data['student_number']
        if Student.objects.filter(student_number=student_number).exists():
            raise ValidationError('A student with this number already exists.')
        return student_number

    def clean_grade_year(self):
        grade_year = self.cleaned_data['grade_year']
        try:
            grade_year = int(grade_year)
        except ValueError:
            raise ValidationError("Grade Year must be a valid number.")

        if grade_year < 1 or grade_year > 6:
            raise ValidationError('Grade Year must be between 1 and 6.') 
        return grade_year

