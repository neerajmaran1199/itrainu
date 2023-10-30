from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import Student
from .forms import StudentForm
# Create your views here.

def Home(request):
    return render(request, 'myapp/home.html')


def create_student(request):
    form = StudentForm(request.POST)
    if request.method == 'POST':
        form.save()
    
    context = {'form':form}
    return render(request, 'myapp/register.html', context)


class CreateStudent(CreateView):
    model = Student

    fields = ['name', 'rollno']
    template_name = 'myapp/register.html'

    
            