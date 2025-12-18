from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def navbar(request):
    return render(request,'navbar.html')

def sample3(request):
    name = request.GET.get("name")
    return HttpResponse(f"<h1>HELLO {name}</h1>")

def sample(request):
    return HttpResponse("<h1>welcome to django</h1>")

def sample1(request):
    return JsonResponse({"data":['friz','tv','washingmachine']})

def sample2(request):
    info={"data":[{"name":"TOM","city":"HYD","gender":"male"},{"name":"Kaveri","city":"Vij","gender":"female"},{"name":"Gowthami","city":"hyd","gender":"female"}]}
    return JsonResponse(info)

def product(request):
    product_name = request.GET.get("product","mobile")
    quantity=request.GET.get("quantity",1)
    price=request.GET.get("price",25000)
    data={"product":product_name,"quantity":quantity,"price":price}
    return JsonResponse(data)

def filteringData(request):
    data = [1,2,3,4,5,6,7,8,9,10]
    filteredData = []
    qp = int(request.GET.get("num",2))
    for x in data:
        if x%qp == 0:
            filteredData.append(x)
    return JsonResponse({"data":filteredData})

def filterStudentsByCity(request):
    student_data = [{"name":"TOM","city":"hyd","gender":"male"},{"name":"Kaveri","city":"Vij","gender":"female"},{"name":"Gowthami","city":"hyd","gender":"female"},{}]
    filteredStudents = []
    city = request.GET.get("city","hyd")
    for student in student_data:
        if student["city"] == city:
            filteredStudents.append(student)
    return JsonResponse({"status":"success","data":filteredStudents})
    