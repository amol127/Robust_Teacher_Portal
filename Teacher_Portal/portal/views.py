from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student
from django.db.models import F

# Login view
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'portal/login.html')

# Logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# Home/student listing view
@login_required
def home(request):
    students = Student.objects.all()
    return render(request, 'portal/home.html', {'students': students})

# Add student view
@login_required
def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        marks = request.POST.get('marks')
        if not (name and subject and marks):
            messages.error(request, 'All fields are required.')
            return redirect('home')
        try:
            marks = int(marks)
        except ValueError:
            messages.error(request, 'Marks must be a number.')
            return redirect('home')
        student, created = Student.objects.get_or_create(name=name, subject=subject, defaults={'marks': marks})
        if not created:
            student.marks = F('marks') + marks
            student.save()
            student.refresh_from_db()
            messages.success(request, f"Updated marks for {name} in {subject}.")
        else:
            student.marks = marks
            student.save()
            messages.success(request, f"Added new student: {name} ({subject}).")
        return redirect('home')
    return redirect('home')

# Edit student view
@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        marks = request.POST.get('marks')
        if not (name and subject and marks):
            messages.error(request, 'All fields are required.')
            return redirect('home')
        try:
            marks = int(marks)
        except ValueError:
            messages.error(request, 'Marks must be a number.')
            return redirect('home')
        # Check for unique constraint
        if Student.objects.exclude(id=student_id).filter(name=name, subject=subject).exists():
            messages.error(request, 'A student with this name and subject already exists.')
            return redirect('home')
        student.name = name
        student.subject = subject
        student.marks = marks
        student.save()
        messages.success(request, 'Student details updated.')
        return redirect('home')
    return render(request, 'portal/edit_student.html', {'student': student})

# Delete student view
@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted.')
        return redirect('home')
    return render(request, 'portal/delete_student.html', {'student': student})
