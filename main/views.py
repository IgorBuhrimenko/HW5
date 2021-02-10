from django.shortcuts import render
from .models import Lecturer, Student, Group


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})


def show_student(request):
    students = Student.objects.all().order_by()
    return render(request, 'main/students.html', {'title': 'Студенты', 'students': students})


def show_lector(request):
    lecturers = Lecturer.objects.all().order_by()
    return render(request, 'main/lector.html', {'title': 'Преподователи', 'lecturers': lecturers})


def show_group(request):
    groups = Group.objects.all().order_by()
    return render(request, 'main/group.html', {'title': 'Курсы', 'groups': groups})


