from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        # model to use for storing data
        model = Student
        # fields to use in the form
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
        # labels to use for the fields
        labels = {
            'student_number': 'Student Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_study': 'Field Of Study',
            'gpa': 'GPA'
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'field_of_study': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'gpa': forms.NumberInput(attrs={
                'class': 'form-control'
            })
        }
        