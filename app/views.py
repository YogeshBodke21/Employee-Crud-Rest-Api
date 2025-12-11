#New Logic
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .forms import Employee_form
from .models import Employee, Department
from datetime import datetime
from django.template.loader import render_to_string
from .tasks import *


def home_view(request):
    return render(request, 'home/home.html', locals())

@login_required
def employeeView(request):
    # If employee profile does NOT exist --> ask user to create it
    if not hasattr(request.user, "employee_profile"):
        messages.success(request, "You do not have profile, first create it to move forward!")
        return redirect("add_emp")

    emp = Employee.objects.all()
    return render(request, 'home/index.html', {"emp": emp})


@login_required
def add_emp_view(request):
    # Block employees from creating second profile
    if hasattr(request.user, 'employee_profile'):
        messages.error(request, "You already have an employee profile.")
        return redirect("emp")

    form = Employee_form()

    if request.method == "POST":
        form = Employee_form(request.POST, request.FILES)

        if form.is_valid():
            emp = form.save(commit=False)
            emp.user = request.user     # Link logged-in user -> Employee
            emp.save()

            # Send email using celery
            email = emp.email
            user = emp.first_name + " " + emp.last_name
            user_info =  request.user.employee_profile
            user_manager = Employee.objects.filter(Designation__name ="Manager" , Department__name = user_info.Department.name ).first()
            print("----", user_manager)
            manager_email = user_manager.email
            print("----", manager_email)
            if manager_email:
                html_manager = render_to_string("home/manager_mail_template.html", {"data": {"User": user, "manager":user_manager}})
                send_mail_to_manager.delay(manager_email, html_manager)
                print("mail sent to manager!")
            html_content = render_to_string("home/my_email.html", {"data": {"User": user}})
            send_html_mail_task.delay(email, html_content)

            messages.success(request, "Employee profile has been created successfully and email has sent to user and respective manager!")
            return redirect("emp")

    return render(request, "home/add_emp.html", {"form": form})


@login_required
def delete_view(request, pk):
    emp = Employee.objects.get(pk=pk)

    # Only HR or Sr. HR Manager can delete employee profile
    designation = request.user.employee_profile.Designation.name

    if designation not in ["Sr. HR Manager"]:
        return HttpResponseForbidden("You do not have permission to delete employees.")

    if request.method == "POST":
        emp.delete()
        messages.success(request, "Employee deleted successfully!")
        return redirect("emp")

    return render(request, "home/index.html")


@login_required
def update_view(request, pk):
    #obj = get_object_or_404(Employee, pk=pk)
    obj = Employee.objects.get(pk=pk)
    user_designation = request.user.employee_profile.Designation.name
    form = Employee_form(instance=obj)
    if user_designation != "Manager" and request.user.employee_profile.first_name != obj.first_name:
        messages.error(request, "You can only edit your own profile.")
        return redirect("emp")
    if request.method == "POST":
          form = Employee_form(request.POST, request.FILES, instance=obj, user=request.user)
          if form.is_valid():
               employee = form.save(commit=False)
               if request.user.employee_profile.Designation.name != "Manager":
                    employee.salary = obj.salary
                    employee.bonus = obj.bonus
               employee.save()
               messages.success(request, "Employee updated successfully!")
               return redirect("emp")    
    else:
          form = Employee_form(instance=obj, user=request.user)
    return render(request, "home/add_emp.html", {"form": form})



#Dashboard for Manager and Sr. HR
@login_required
def dashboard_view(request):
    user_designation = ""
    if hasattr(request.user, "employee_profile") and request.user.employee_profile.Designation:
        user_designation = request.user.employee_profile.Designation.name

    dept_stats = []
    total_salary = 0
    total_bonus = 0

    # Only HR/Manager can see financial stats
    if user_designation in ["Sr. HR Manager", "Manager"]:
        departments = Department.objects.all()
        for dept in departments:
            print(dept)
            stats = Employee.objects.filter(Department=dept).aggregate(
                dept_salary=Sum('salary'),
                dept_bonus=Sum('bonus')
            )
            print(stats)
            dept_salary = stats['dept_salary'] or 0
            dept_bonus = stats['dept_bonus'] or 0

            total_salary += dept_salary
            total_bonus += dept_bonus

            dept_stats.append({
                "name": dept.name,
                "salary": dept_salary,
                "bonus": dept_bonus,
                "employee_count": Employee.objects.filter(Department=dept).count()
            })
        print("dept_stats ---", (dept_stats))
        emps = Employee.objects.count()
    return render(request, "home/dashboard.html", {
        "user_designation": user_designation,
        "dept_stats": dept_stats,
        "total_salary": total_salary,
        "total_bonus": total_bonus,
        "Total" : emps
    })



'''
#simple way without template
send_mail("Mail via Django", "you have been added to list.", settings.EMAIL_HOST_USER, ['ybodke123@gmail.com'])'''


#celery cmd ---celery -A myproject worker --loglevel=info #this doesnt work on windows

#celery -A your_project_name worker --pool=solo -l info  #Use solo pool (good for development or small projects) do not support multiprocessing

#so achieve this via threads ---> celery -A your_project_name worker --pool=threads -l info


