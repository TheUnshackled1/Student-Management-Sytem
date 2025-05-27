from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponseRedirect
from .models import Student
from .forms import StudentForm
from django.urls import reverse
from django.contrib import messages 

# This view renders the index page, displaying all students from the database
def index(request):
    return render(request, 'index.html', {
        'students': Student.objects.all()
    })

# This view handles the display of a single student's information. 
# (Currently redirects to the 'index' page after viewing the student.)
def view_student(request, id):
    student = Student.objects.get(pk=id)  # Retrieve student by primary key (id)
    return HttpResponseRedirect(reverse('index'))  # Redirects to the index page

# This view handles the creation of a new student. 
# It checks for duplicates and saves the new student if no duplicates are found.
def add(request):
    form = StudentForm()  # Create a blank form
    if request.method == "POST":  # Check if the form was submitted
        form = StudentForm(request.POST)  # Bind the form with POST data
        if form.is_valid():  # Check if the form data is valid
            new_student_number = form.cleaned_data['student_number']
            
            # Check if a student with the same student_number already exists
            if Student.objects.filter(student_number=new_student_number).exists():
                messages.error(request, "A student with this number already exists.")
                return redirect('add')  # Redirect to the add page if duplicate exists
            
            # Validate grade_year manually
            grade_year = form.cleaned_data['grade_year']
            if grade_year < 1 or grade_year > 6:
                messages.error(request, "Grade Year must be between 1 and 6.")
                return render(request, 'add.html', {'form': form})

            # Extract cleaned data
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_subject = form.cleaned_data['subject']
            new_grade_year = form.cleaned_data['grade_year']
            new_grade = form.cleaned_data['grade']

            # Create and save the new student object
            new_student = Student(
                student_number=new_student_number,
                first_name=new_first_name,
                last_name=new_last_name,
                subject=new_subject,
                grade_year=new_grade_year,
                grade=new_grade
            )
            new_student.save()
            return render(request, 'add.html', {
                'form': StudentForm(),
                'success': True
            })
        else:
            messages.error(request, "There was an error with the form submission.")  # Show error if invalid
    return render(request, 'add.html', {'form': form})  # Render the add page with the form

# This view handles editing an existing student's information.
def edit(request, id):
    if request.method == "POST":  # Check if the form was submitted
        student = Student.objects.get(pk=id)  # Retrieve student by ID
        form = StudentForm(request.POST, instance=student)  # Bind form with POST data and student's current data
        if form.is_valid():  # Check if the form data is valid
            form.save()  # Save the changes
            return render(request, 'edit.html', {
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=id)  # Retrieve student by ID
        form = StudentForm(instance=student)  # Pre-fill the form with the student's data
    return render(request, 'edit.html', {'form': form})

# This view handles the deletion of a student.
def delete(request, id):
    if request.method == "POST":  # Confirm that the request is a POST request before deletion
        student = Student.objects.get(pk=id)  # Retrieve student by ID
        student.delete()  # Delete the student record
    return HttpResponseRedirect(reverse('index'))  # Redirect to the index page after deletion

# This view handles user login.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('index')  # Redirect after login
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')

    return render(request, 'login.html')
