# from .views import employeeView, employeeDetailView
# from .views import ClassBasedApiView, EmployeeDetailsView, 
# from .views import Employees, EmployeeDetailsView
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDestroyAPIView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # path("emps/", employeeView),
    # path("emps/<int:pk>", employeeDetailView),


    # #class based
    # path("emps/", ClassBasedApiView.as_view()),
    # path("emps/<int:pk>", EmployeeDetailsView.as_view()),

    #mixins urls
    #  path("emp/", Employees.as_view()),
    #  path("emp/<int:pk>", EmployeeDetailsView.as_view()),


     #generics urls
     
    path("emp/", EmployeeListCreateView.as_view()),
    path("emp/<int:pk>", EmployeeRetrieveUpdateDestroyAPIView.as_view()),
    path("api/token/", obtain_auth_token),
    path('api/jwttoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/jwttoken/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]