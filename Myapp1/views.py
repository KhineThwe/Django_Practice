from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import AuthorForm
from .models import Author
# Create your views here.

def home(request):
    context={}
    #return HttpResponse("Hello World!")
    return render(request,'index.html',context)
    
def author_list(request):
    authors = Author.objects.all()
    context = {"authors":authors}
    return render(request,'author_list.html',context)

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST,request.FILES)#takes as json type
        if form.is_valid():
            form.save()
            return redirect('list_author')
    else:
        form = AuthorForm()
    return render(request,'author_form.html',{'form':form,'action':'Create'})

def author_delete(request,id):
    Author.objects.get(id=id).delete()
    return redirect('list_author')

def author_update(request,id):
    author = Author.objects.get(id=id)
    form = AuthorForm(instance=author)
    return render(request,'author_form.html',{'form':form,'action':'Update'})

def book_list(request):
    return render(request,'book_list.html')

def student_list(request):
    return render(request,'student_list.html')

def course_list(request):
    return render(request,'course_list.html')