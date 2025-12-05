from django.shortcuts import render, redirect
from .models import Employee
from .forms import Employee_form


# Create your views here.
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
        

def add_emp_view(request):
     template_name = "home/add_emp.html"
     print("----")
     form = Employee_form()
     if request.method == "POST":
          form = Employee_form(request.POST, files=request.FILES)
          if form.is_valid():
               form.save()
               print("----  added!")
               return redirect("emp")
     return render(request, template_name, locals())  


def delete_view(request, pk):
    print(pk)
    emp = Employee.objects.get(pk=pk)
    if request.method == "POST":
         emp.delete()
         return redirect("emp")
    return render(request, 'home/index.html')


def update_view(request, pk):
     obj = Employee.objects.get(pk=pk)
     form = Employee_form(instance=obj)
     if request.method == "POST":
          form = Employee_form(request.POST, files = request.FILES)
          if form.is_valid():
               form.save()
               return redirect("emp")
     template_name = "home/add_emp.html"
     return render(request, template_name, locals())
