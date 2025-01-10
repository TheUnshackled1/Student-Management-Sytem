from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from .models import Student
from .forms import StudentForm
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'index.html',
    {
        'students': Student.objects.all()
    })
def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))
def add(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_subject = form.cleaned_data['subject']
            new_grade_year = form.cleaned_data['grade_year']
            new_grade = form.cleaned_data['grade']
#----------------------------------------------------------#      
            new_student = Student(
                student_number=new_student_number,
                first_name=new_first_name,
                last_name=new_last_name,
                subject=new_subject,
                grade_year=new_grade_year,
                grade=new_grade
            )
            new_student.save()
            return render(request,'add.html', {
                'form': StudentForm(),
                'success': True
            })
        else:
            form = StudentForm()
    return render(request, 'add.html', {'form': form})
def edit(request, id):
    if request.method == "POST":
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'edit.html', {
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'edit.html', {
        'form': form, })
def delete(request, id):
    if request.method == "POST":
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))