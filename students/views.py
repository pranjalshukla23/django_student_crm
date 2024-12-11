from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def index(request):
    # render a template
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })
    
    
def view_student(request, id):
    # get the student by id (primary key)
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == "POST":
        # create an instance of student form with user input data
        form = StudentForm(request.POST)
        if form.is_valid():
            # extract the cleaned field values from  the form
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']
            
            # create an instance of Student
            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study,
                gpa = new_gpa
            )
            
            # save the student record
            new_student.save()
            
            # render a template
            return render(request, 'students/add.html', {
                'form': form,
                'success': True
            })
    else:
        # create an empty instance of student form
        form = StudentForm()
        # render a template
        return render(request, 'students/add.html', {
            'form': form
        })
        
def edit(request, id):
    if request.method == 'POST':
        # get student by id (primary key)
        student = Student.objects.get(pk=id)
        # create an instance of student form with user input data and prepopulate the form with the student info we get from db
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            # save the student record in db
            form.save()
            # render a template
            return render(request, 'students/edit.html',{
                'form': form,
                'success': True
            })
    else:
        # get student by id (primary key)
        student = Student.objects.get(pk=id)
        # create an instance of student form and prepopulate the form with the student info we get from db
        form = StudentForm(instance=student)
        return render(request, 'students/edit.html', {
            'form': form
        })
        
def delete(request, id):
    if request.method == 'POST':
        # get the student by id (primary key)
        student = Student.objects.get(pk=id)
        # delete the student from db
        student.delete()
    return HttpResponseRedirect(reverse('index'))
            
            

