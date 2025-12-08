from django.urls import path
from .views import employeeView, add_emp_view, delete_view, update_view, dashboard_view, home_view
from auth.views import signUpView, login_view, logout_view
urlpatterns = [
    path("home/", home_view, name="home"),
    path('emp/', employeeView, name='emp' ),
    path('add_emp/', add_emp_view, name='add_emp' ),
    path('del_emp/<int:pk>', delete_view, name='del_emp' ),
    path('up_emp/<int:pk>', update_view, name='up_emp' ),
    path('signup/', signUpView, name='signup' ),
    path('login/', login_view, name='login' ),
    path('logout/', logout_view, name='logout' ),
    path('dashboard/', dashboard_view, name='dashboard' ),
    
    

]