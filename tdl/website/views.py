from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
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
        return render(request, 'home.html')
    
def logout_user(request):
    logout(request)
    return redirect('home')

def register(request):
    pass

