from django.shortcuts import render, redirect
from .models import Employee
from .forms import Employee_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def employeeView(request):
        template_name = 'home/index.html'
        if request.method == 'GET':
            emp = Employee.objects.all()
            context = {'emp': emp}
            return render(request, template_name, context)
        if request.method == 'POST':
            emp = Employee.objects.all()
            context = {'emp': emp}
            return render(request, template_name, context)
        
@login_required()
def add_emp_view(request):
     template_name = "home/add_emp.html"
     print("----")
     form = Employee_form()
     if request.method == "POST":
          form = Employee_form(request.POST, files=request.FILES)
          if form.is_valid():
               form.save()
               print("----  added!")
               messages.success(request, "One employee has been added successfully!")
               return redirect("emp")
     return render(request, template_name, locals())  

@login_required()
def delete_view(request, pk):
    print(pk)
    emp = Employee.objects.get(pk=pk)
    if request.method == "POST":
         emp.delete()
         messages.success(request, "One employee has been deleted successfully!")
         return redirect("emp")
    return render(request, 'home/index.html')

@login_required()
def update_view(request, pk):
     obj = Employee.objects.get(pk=pk)
     form = Employee_form(instance=obj)
     if request.method == "POST":
          form = Employee_form(request.POST, files = request.FILES, instance=obj)
          if form.is_valid():
               form.save()
               messages.success(request, "One employee has been updated successfully!")
               return redirect("emp")
     template_name = "home/add_emp.html"
     return render(request, template_name, locals())
