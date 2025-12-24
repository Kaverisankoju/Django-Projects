from decimal import Decimal
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import math
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import BookInfo, CourseRegistration, MovieTicketBooking, OrderDetails, ProductDetails, userProfile,Employee
from django.db.utils import IntegrityError



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

def pagination(request):
    data = ['apple','banana','carrot','grapes','watermelon','kiwi','pineapple','custard-apple','strawberry','blueberry']
    page = int(request.GET.get("page",1))
    limit = int(request.GET.get("limit",3))
    
    start = (page-1)*limit
    end = page*limit
    total_pages = math.ceil(len(data)/limit)
    result = data[start:end]
    
    res = {"status":"success","current_page":page,"total_pages":total_pages,"data":result}
    return JsonResponse(res)

@csrf_exempt
def createData(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body) #dictionary
            name = data.get("name") #name from dict
            age = data.get("age")
            city = data.get("city")
            userProfile.objects.create(name=name,age=age,city=city)
            print(data)
        return JsonResponse({"status":"success","data":data,"statuscode":201},status = 201)
    except Exception as e:
        return JsonResponse({"statuscode":500,"message":"internal server error"})

@csrf_exempt
def createProduct(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
    return JsonResponse({"status":"success","data":data,"statuscode":201}) 

@csrf_exempt
def createEmployee(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            Employee.objects.create(emp_name=data.get("name"),emp_salary=data.get("salary"),emp_email=data.get("email"))  
            print(data)
            return JsonResponse({"status":"success","data":data,"statuscode":201})   
    except IntegrityError as e:
        return JsonResponse({"statuscode":"error","message":"dublicate values are not allowed"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"error","message":"something went wrong"})
    finally:
        print("DONE")

@csrf_exempt
def createProductDetails(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            product = ProductDetails.objects.create(
                prod_name=data.get("name"),
                prod_price=data.get("price"),
                prod_quantity=data.get("quantity")
            )

            return JsonResponse({
                "status": "success",
                "data": {
                    "name": product.prod_name,
                    "price": product.prod_price,
                    "quantity": product.prod_quantity,
                    "total_price": product.total_price
                },
                "statuscode": 201
            }, status=201)

        return JsonResponse({
            "status": "error",
            "message": "Only POST method allowed"
        }, status=405)

    except IntegrityError:
        return JsonResponse({
            "status": "error",
            "message": "Duplicate values are not allowed"
        }, status=400)

    except Exception as e:
        print(e)
        return JsonResponse({
            "status": "error",
            "message": "Something went wrong"
        }, status=500)

    finally:
        print("DONE")
 
        
def carPrices(request):
    qp = int(request.GET.get("price",100000))
    qp1 = request.GET.get("car_type","bmw")
    
    if qp > 3000000:
        msg = "omg"
    elif qp < 200000 and qp > 50000:
        msg ="avvadhu le"
    else:
        msg ="nice"
    return HttpResponse(msg)


# POST METHOD
@csrf_exempt
def orderPlacing(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            order = OrderDetails.objects.create(
                orderid = data["order_id"],
                useremail = data["email"],
                amount = Decimal(str(data["amount"])),
                status = data["status"],
                mode = data["mode"]
            )
            print(order.transaction_id)
            x = str(order.transaction_id)
            return JsonResponse({
                "status":"success",
                "message":"payment details updated successfully",
                "transaction_id":x
            },status = 201)
        else:
            return JsonResponse({"error":"only post method is allowed"},status = 400)
    except Exception as e:
        print(e)
        return JsonResponse({"error":"something went wrong"},status = 500)
 
 
   
@csrf_exempt
def movieTickets(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            ticket = MovieTicketBooking.objects.create(
                moviename = data["movie_name"],
                showtime = data["show_time"],
                screename = data["screen_name"]
            )
            print(ticket.trasactionid)
            x = str(ticket.trasactionid)
            return JsonResponse({
                "status":"success",
                "message":"movie ticket is confimed",
                "transaction_id":x
            },status = 201)
        else:
            return JsonResponse({"error":"wrong movie ticket"},status = 400)
            
    except Exception as e:
        print(e)
        return JsonResponse({"error":"check the details once"},status = 500)
  
  
#GET METHOD  
@csrf_exempt
def getOrders(request):
    try:
        if request.method == 'GET':
            result = list(OrderDetails.objects.values())
            if len(result) == 0:
                msg = "No records found"
            else:
                msg = "Data retriving is successfully"
            return JsonResponse({"status":"success","message":msg,"data":result,"lenght of data":len(result)})
        return JsonResponse({"message":"use only get method"})
    except Exception as e:
        print(e)
        return JsonResponse({"error":"something went wrong"})                
   

#  PATH PARAMS
student_info = [{"id":1,"name":"kaveri"},{"id":2,"name":"Adarsh"},{"id":3,"name":"Riveka"}]
def getStudentById(request,id):
    filteredStudent = []
    for student in student_info:
        if id == student["id"]:
            filteredStudent.append(student)
    return JsonResponse({"data":filteredStudent})



@csrf_exempt
def postBookDetails(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            bookdetails = BookInfo.objects.create(
               bookname = data["book_name"],
               authorName = data["author"],
               category = data["category"],
               price = str(data["price"]),
               rating = str(data["rating"])  
            )
            return JsonResponse({"status":"success","message":"data retrived successfully","data":data})
        return JsonResponse({"message":"check the details once"})
    except Exception as e:
        print(e)
        return JsonResponse({"error":str(e)})
    
    
def getbookInfo(request):
    try:
        if request.method == 'GET':
            result = list(BookInfo.objects.values())
            if len(result) == 0:
                msg = "No records found"
            else:
                msg = "Data retriving is successfully"
            return JsonResponse({"status":"success","message":msg,"data":result,"length of data":len(result)})
        return JsonResponse({"message":"use only get method"})  
    except Exception as e:
        print(e)
        return JsonResponse({"error":"something went wrong"}) 
   
@csrf_exempt 
def  courseRegister(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            register = CourseRegistration.objects.create(
                name = data["name"],
                email = data["email"],
                course = data["course"],
                phone = data["phone"]
            )
            return JsonResponse({"status":"success","message":"Registration successful"},status = 201)
        return JsonResponse({"message":"check the details once"},status = 400)
    except Exception as e:
        print(str(e))
        return JsonResponse({"error":"something went wrong"},status = 500)  
    
    
def getRegisterDetails(request):
    try:
        if request.method == 'GET':
            result =  list(CourseRegistration.objects.values())   
            if len(result) == 0:
                msg = "No records found"
            else:
                msg = "Data retriving is successfully"
            return JsonResponse({"status":"success","message":msg,"data":result},status = 201)
        return JsonResponse({"message":"use only get method"})
    except Exception as e:
        print(e)
        return JsonResponse({"error":"something went wrong"})
    
    
            

                
                
            
    
    