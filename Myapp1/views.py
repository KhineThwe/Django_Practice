from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import AuthorForm,UserRegisterForm,StudentForm,CourseForm
from .models import Author,Student,Course
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import MessageSerializers
# Create your views here.

@login_required
def home(request):
    context={}
    #return HttpResponse("Hello World!")
    return render(request,'index.html',context)

@login_required
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('home')
        else:
            print(form.errors)
    else:   
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})

@login_required  
def author_list(request):
    authors = Author.objects.all()
    context = {"authors":authors}
    return render(request,'author_list.html',context)

@login_required
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST,request.FILES)#takes as json type
        if form.is_valid():
            form.save()
            return redirect('list_author')
    else:
        form = AuthorForm()
    return render(request,'author_form.html',{'form':form,'action':'Create'})

@login_required
def author_delete(request,pk):
    author = get_object_or_404(Author,pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('list_author')
    return render(request,'author_confirm_delete.html',{'author':author})

@login_required
def author_update(request,pk):
    author = get_object_or_404(Author,pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST,request.FILES,instance=author)#takes as json type
        if form.is_valid():
            form.save()
            return redirect('list_author')
    else:
        form = AuthorForm(instance=author)
    return render(request,'author_form.html',{'form':form,'action':'Update'})
    
@login_required
def book_list(request):
    return render(request,'book_list.html')

@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request,'add_student.html',{'form':form,'action':'Create'})

@login_required
def student_list(request):
    students = Student.objects.all()
    context = {"students":students}
    return render(request,'student_list.html',context)

@login_required
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request,'add_course.html',{'form':form,'action':'Create'})

@login_required
def course_list(request):
    courses = Course.objects.all()
    context = {"courses":courses}
    return render(request,'course_list.html',context)

def send_message(request):
    students = Student.objects.all()
    return render(request,'send_message.html',{'students':students})