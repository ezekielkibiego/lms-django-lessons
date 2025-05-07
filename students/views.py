from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def index(request):

    ctx = {'name': 'John Doe'}
    return render(request, 'index.html', ctx)

def students_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    
    return render(request, 'students_list.html', ctx)
