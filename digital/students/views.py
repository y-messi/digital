from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Student, Category, Product
from .forms import StudentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {'students': Student.objects.all()})

def view_student(request):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))
    
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_title = form.cleaned_data['title']
            new_author = form.cleaned_data['author']
            new_date = form.cleaned_data['date']
            new_shelve = form.cleaned_data['shelve']
           
            new_student = Student(
                title=new_title,
                author=new_author,
                date=new_date,
                shelve=new_shelve,
            )
            new_student.save()
            return render(request, 'add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    return render(request, 'add.html', {'form': form})


def edit(request, id):
    if request.method == 'POST':
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
        'form': form
    })             
            
def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))    


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully.")
            return redirect('index')  # Ensure 'index' is the correct URL name
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login')
    
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out..... Thanks for spending some time with us"))
    return redirect('login')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # authenticate user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been registered successfully! Welcome!")
                return redirect('login')  # Make sure 'login' is the correct URL name
            else:
                messages.error(request, "Authentication failed. Please try again.")
                return redirect('register')
        else:
            messages.error(request, "There was a problem with your registration. Please check the form and try again.")
            # Optionally, render the form with errors back to the user
            return render(request, 'register.html', {'form': form})
    else:    
        return render(request, 'register.html', {'form': form})

def category(request, foo):
    # replace hyphens with spaces
    foo = foo.replace('-', '')
    # grab the category from the url
    
    try:
        #look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    except:
        messages.success(request, ("That Category Doesnot Exist........."))
        return redirect('index')                    
    
def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})    