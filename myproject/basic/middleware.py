# MIDDLEWARES ARE TWO TYPES
# GLOBAL,SPECIFIC MIDDLEWARE
# 1-->GLOBAL MIDDLEWARE
import re
from django.http import HttpResponse,JsonResponse
import json
from typing import Any
from django.http import HttpResponse

# from myproject.basic.models import User
from basic.models import User


class middleware1:
    def __init__(self,get_response):
        print("middleware1 initiates")
        self.get_response = get_response
    def __call__(self,request):
        print("middleware1 get the response")
        response = self.get_response(request)
        return response



# SPECIFIC MIDDLEWARE


class middleware2:
    def __init__(self,get_response):
        print("middleware2 initiates")
        self.get_response = get_response
    def __call__(self,request):
        if request.path != "/home/":
            return HttpResponse("Access Denied", status=403)
        return self.get_response(request)



# ANOTHER WAY

class middleware3:
    def __init__(self,get_response):
        print("middleware1 initiates")
        self.get_response = get_response
    def __call__(self,request):
        if request.path == '/about/':
            print("middleware1 get the response")
            response = self.get_response(request)
            return response
        
        
class sccMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        if (request.path == '/job1/') and (request.method == 'POST'):
            input_data = json.loads(request.body)
            ssc_status = input_data.get("ssc_status")
            if not ssc_status:
                return JsonResponse({
                    "status": "failure",
                    "msg": "You should pass SSC to apply for this job"
                }, status=403)

        return self.get_response(request)
            
        
class medicalStatusMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        if (request.path == '/job1/') and (request.method == 'POST'):
            input_data = json.loads(request.body)
            medical_status = input_data.get("medically_fit")
            if not medical_status:
                return JsonResponse({
                    "status": "failure",
                    "msg": "You should be medically fit to apply"
                }, status=403)

        return self.get_response(request)
        
        
        
class ageValidationMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        if (request.path == '/job1/') and (request.method == 'POST'):
            input_data = json.loads(request.body)
            age = input_data.get("age")
            if age is None or age <= 21:
                return JsonResponse({
                    "status": "failure",
                    "msg": "Age must be above 21"
                }, status=403)

        return self.get_response(request)
            
        
class interValidation:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        if request.path == '/engineeringSeat/' and request.method == 'POST':
            input_data = json.loads(request.body)
            inter_status = input_data.get("inter_qualify")
            if inter_status:
                return self.get_response(request)
            return JsonResponse({"status":"failure","msg":"u should pass inter to get engineering seat"})
        
class eamcetValidation:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self,request):
        if request.path == '/engineeringSeat/' and request.method == 'POST':
            input_data = json.loads(request.body)
            eamcet_status = input_data.get("eamcet_qualify")
            if eamcet_status:
                return self.get_response(request)
            return JsonResponse({"status":"failure","msg":"u need to pass the eamcet to get the engineerig seat"})
        
        
        
USERNAME_REGEX = r'^[a-zA-Z0-9_]{4,20}$'
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}$'
PASSWORD_REGEX = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'

class UsernameValidationMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self,request):
        if request.path == '/signup/' and request.method == 'POST':
            data = json.loads(request.body)
            username = data.get('username')
            
            
            if not re.match(USERNAME_REGEX,username):
                return JsonResponse({"error":"Invalid username format"})
            
            if User.objects.filter(username = username).exists():
                return JsonResponse({"error":"Username already exists"})
        return self.get_response(request)
    
    
class EmailValidationMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        if request.path == '/signup/' and request.method == 'POST':
            data = json.loads(request.body)
            email = data.get("email")
            
            if not re.match(EMAIL_REGEX,email):
                return JsonResponse({"error":"invalid email format"})
            if User.objects.filter(email = email).exists():
                return JsonResponse({"error":"Email already exists"})
        return self.get_response(request)
    
    
class PasswordValidationMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self,request):
        if request.path == '/signup/' and request.method == 'POST':
            data = json.loads(request.body)
            password = data.get('password')
            
            if not re.match(PASSWORD_REGEX,password):
                return JsonResponse({"error":'password must be strong(8 chars,uppercase,lowercase,numbers,special char)'})   
        return self.get_response(request)
        