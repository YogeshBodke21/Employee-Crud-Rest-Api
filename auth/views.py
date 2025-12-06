from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here:
def signUpView(request):
    print("accepted1!")
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("user logined!")
            
            return redirect("login")
        #else:
            #messages.error(request, "Invalid Input Data..! Please try again.")
    template_name = 'home/signup.html'
    return render(request, template_name, locals())


def login_view(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        pw = request.POST.get('passw')
        user = authenticate(username=un, password=pw)
        print('user----', user)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('emp')
        else:
            print('else--->user----', user)
            messages.error(request,"Invalid Input Data. Please try again!")
    return render(request, 'home/login.html')

def logout_view(request):
    logout(request)
    return redirect ('login')
