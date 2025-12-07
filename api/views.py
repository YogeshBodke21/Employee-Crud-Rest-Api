from django.shortcuts import render
from app.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics

#Authentication
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

#Token Authentication
from rest_framework.authtoken.models import Token

#JWT Auth
from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.parsers import MultiPartParser, FormParser # for media acceptance
# Create your views here.



#Function based views to perform CRUD operations.

"""
@api_view (['GET', 'POST'])
@authentication_classes([BasicAuthentication, TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def employeeView(request):
    if request.method == "GET":
        Employees = Employee.objects.all()
        serializer = EmployeeSerializer(Employees, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            print("###################")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
@api_view (['GET', 'PUT', 'DELETE'])
def employeeDetailView(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
"""



'''
Class based views to perform CRUD operations.

'''

# class ClassBasedApiView(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self, request):
#         #employees = Employee.objects.all()
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

# class EmployeeDetailsView(APIView):
#     def get_employee(self, pk):
#         try:
#             employee = Employee.objects.get(pk=pk)
#             return employee
#         except Employee.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk):
#         employee = self.get_employee(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def put(self, request, pk):
#         employee = self.get_employee(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        
#     def delete(self, request, pk):
#         employee = self.get_employee(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    


"""
Mixins views for all methods.

# """
# class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
# class EmployeeDetailsView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#     def put(self, request, pk):
#         return self.update(request, pk)
#     def delete(self, request, pk):
#         return self.destroy(request, pk)
  

#Generics
class EmployeeListCreateView(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "pk"
















