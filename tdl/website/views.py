from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import ToDoItem

from website.forms import SignUpForm, AddItemForm
# Create your views here.

def home(request):
    #get all items
    items = ToDoItem.objects.all()
    
    #check if user already logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request , username=username , password= password)
        #if all is right
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Faild to log in successfully!')
            return redirect('home')
    else:
        return render(request, 'home.html', {'items': items})
    
def logout_user(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        #here we pass the post request because the already filled out the form
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,'You have been succesfully signed up!')
            return redirect('home')
    else:
            #here we dont pass anything because they didnt fill out the form yet
            form = SignUpForm()
            return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

def toDoItem(request, pk):
    if request.user.is_authenticated:
     # look up record   
            tdItem = ToDoItem.objects.get(id=pk)
            return render(request, 'item.html', {'tdItem': tdItem})
    else:
        messages.error(request, "you must be logged In!")
        return redirect('home')
    
def delete_item(request,pk):
    if request.user.is_authenticated:
     # look up record   
            tdItem = ToDoItem.objects.get(id=pk)
            tdItem.delete()
            #messages.success('Item was deleted')
            return redirect('home')
    else:
        #messages.error(request, "you must be logged In!")
        return redirect('home')
    
def add_item(request):
    form = AddItemForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request, "add_item.html", {'form':form})
    else:
        return redirect('home')
    
def update_item(request,pk):
    if request.user.is_authenticated:
        current_item = ToDoItem.objects.get(id=pk)
        form = AddItemForm(request.POST or None, instance=current_item)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, "update_item.html", {'form':form})
    else:
        return redirect('home')

        
        

