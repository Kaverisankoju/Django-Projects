# MIDDLEWARES ARE TWO TYPES
# GLOBAL,SPECIFIC MIDDLEWARE
# 1-->GLOBAL MIDDLEWARE
class middleware1:
    def __init__(self,get_response):
        print("middleware1 initiates")
        self.get_response = get_response
    def __call__(self,request):
        print("middleware1 get the response")
        response = self.get_response(request)
        return response



# SPECIFIC MIDDLEWARE

from django.http import HttpResponse

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
            
        