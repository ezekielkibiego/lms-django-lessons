from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django_registration.backends.one_step.views import RegistrationView
from django.urls import reverse_lazy

class CustomRegistrationView(RegistrationView):
    success_url = reverse_lazy('login')  

def index(request):

    ctx = {'name': 'John Doe'}
    return render(request, 'index.html', ctx)

def students_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    
    return render(request, 'students/students_list.html', ctx)
