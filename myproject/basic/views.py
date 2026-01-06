from decimal import Decimal
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import math
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import BookDetails, BookInfo, CourseRegistration, MovieTicketBooking, OrderDetails, ProductDetails, userProfile,Employee
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
 
 
# post the data into the database
@csrf_exempt
def movieTickets(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            ticket = MovieTicketBooking.objects.create(
                moviename = data["movie_name"],
                showtime = data["show_time"],
                screename = data["screen_name"],
                genres = data["genres_type"]
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
        return JsonResponse({"error":str(e)},status = 500)
    


# getting the data
def getMovieDetails(request):
    try:
        if request.method == 'GET':
            result = list(MovieTicketBooking.objects.values())
            if len(result) == 0:
                msg = "no records found"
            else:
                msg = "records fetched successufully"
            return JsonResponse({"status":"success","message":msg,"data":result,"no.of record":len(result)},status = 201)
        return JsonResponse({"status":"pending","message":"only get method is used"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"failure","message":"something went wrong"},status = 500)  
    
    
# filter the data according to the condition by path param
def getMovieByGenres(request,genres_val):
    try:
        if request.method == 'GET':
            data = MovieTicketBooking.objects.filter(genres=genres_val).values()
            filter_data = list(data)
            if not filter_data:
                msg = "no records found"
            else:
                msg = "records fetched successfully"
            return JsonResponse({"status":"success","msg":msg,"data":filter_data,"no. of records":len(filter_data)})  
        return JsonResponse({"message":"only get method is used"})
    except Exception as e:
        return JsonResponse({"status":"failure","message":str(e)})
    
    
def getMovieByScreenname(request,screen_name):
    try:
        if request.method == 'GET':
            data = MovieTicketBooking.objects.filter(screenname=screen_name).values()
            final_result = list(data)
            if len(final_result) == 0:
                msg = "no records found"
            else:
                msg = "record fetched successfully"
            return JsonResponse({"status":"success","data":final_result,"msg":msg},status = 200)
        return JsonResponse({"status":"pending","msg":"only get method allowed"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"error","msg":"something went wrong"},status = 500)
  
  
  
def getMovieByMultipleScreens(request,first,second):
    try:
        if request.method == 'GET':
            data1 = MovieTicketBooking.objects.filter(screenname=first).values()
            data2 = MovieTicketBooking.objects.filter(screenname=second).values()
            first_data = list(data1)
            second_data = list(data2)
            if len(first_data) == 0:
                msg = "no records found"
            else:
                msg = "record fetched successfully"
            if len(second_data) == 0:
                msg = "no records found"
            else:
                msg = "record fetched successfully"
            return JsonResponse({"status":"success",first:first_data,second:second_data,"msg":msg},status = 200)
        return JsonResponse({"status":"pending","msg":"only get method allowed"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"error","msg":"something went wrong"},status = 500)
  
  
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
    
    
student_info1 = [{"id":1,"name":"kaveri","degree":"CSE"},{"id":2,"name":"Tom","degree":"EEE"},{"id":3,"name":"Gowthami","degree":"CIVIL"},{"id":4,"name":"Rammurthy","degree":"CSE"}]    
def getStudentByDegree(request,deg):
    try:
        if request.method == 'GET':
            
            DegreeBasedFilteration = [] 
            for student in student_info1:
                if deg.lower() == student["degree"].lower():
                    DegreeBasedFilteration.append(student)
            if len(DegreeBasedFilteration) == 0:
                msg = "no records found"
            else:
                msg = "student record fetched successfully"
            return JsonResponse({"status":"success","data":DegreeBasedFilteration,"msg":msg,"no. of recods":len(DegreeBasedFilteration)},status=200)
        
        return JsonResponse({"status":"failure","message":"only get method is allowed"},status = 400)
    except Exception as e:
        print(e)
        return JsonResponse({"message":"something went wrong"})
        

def getOrdersByStatus(request,status_param):
    try:
        if request.method == 'GET':
            data = OrderDetails.objects.filter(status=status_param)
            response = []
            for obj in data:
                response.append({"id":obj.orderid,"amount":obj.amount,"mode":obj.mode,"status":obj.status})
            return JsonResponse({"status":"success","msg":"record fetched successfully","data":response},status = 200)
        return JsonResponse({"status":"failure","msg":"only get method is allowed"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"error","msg":str(e)},status = 500)
    
    
@csrf_exempt
def updateMovieScreen(request,screen_name):
    try:
        if request.method =='PUT':
            input_data = json.loads(request.body)
            new_screen = input_data["new_screen"]
            update = MovieTicketBooking.objects.filter(screenname=screen_name).update(screenname=new_screen)
            if update == 0:
                msg = "no record found with reference of id"
            else:
                msg = "record is updated successfully"
            return JsonResponse({"status":"success","msg":msg},status = 200)
        return JsonResponse({"msg":"only put method is allowed"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"failure","msg":"something went wrong","error":str(e)},status = 500)
                
#  UPDATING THE DATA  
@csrf_exempt
def updateUserById(request):
    try:
        if request.method == 'PUT':
            input_data = json.loads(request.body)
            ref_id = input_data["id"]
            new_city = input_data["new_city"]
            
            update = userProfile.objects.filter(id=ref_id).update(city=new_city)
            
            if update == 0:
                msg = "no records founds with the existing id"
            else:
                msg = "record updated successufully"
                
            return JsonResponse({"status":"success","msg":msg},status = 200)
        return JsonResponse({"status":"pending","msg":"only put method is used"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"failure","msg":"something went wrong"},status = 500)
    

@csrf_exempt
def updateUserageById(request):
    try:
        if request.method == 'PUT':
            input_data = json.loads(request.body)
            ref_id = input_data["id"]
            new_age = input_data["new_age"]
            update = userProfile.objects.filter(id = ref_id).update(age = new_age)
            if update == 0:
                msg = "no records founds with the existing id"
            else:
                msg = "record updated successufully"
                
            return JsonResponse({"status":"success","msg":msg},status = 200)
        return JsonResponse({"status":"pending","msg":"only put method is used"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"failure","msg":"something went wrong"},status = 500)
    
#UPDATE DATA BY PATH PARAM 
@csrf_exempt
def updataUserByStatus(request,ref_status):
    try:
        if request.method == 'PUT':
            input_data = json.loads(request.body)
            new_status = input_data["new_status"]
            update = OrderDetails.objects.filter(status = ref_status).update(status = new_status)
            if update == 0:
                msg = "no records found"
            else:
                msg = "record updated successfully"
            return JsonResponse({"status":"success","msg":msg},status = 200)
        return JsonResponse({"status":"pending","msg":"only put method is used"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"failure","msg":"Something went wrong"},status = 500) 



 
# DELET OPERATION 
@csrf_exempt
def deleteUserDataById(request,ref_id):
    try:
        if request.method == 'DELETE':
            delete_data = userProfile.objects.filter(id = ref_id).delete()
            if delete_data[0] == 0:
                msg = "no records found with that reference id"
            else:
                msg = "record deleted successfully"
            return JsonResponse({"status":"success","msg":msg},status = 200)
        return JsonResponse({"status":"pending","msg":"only delete method is used"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"failure","msg":"something went wrong"},status = 500)
    
    
# POST
@csrf_exempt
def postBookDetails(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            book = BookDetails.objects.create(
                id = data["id"],
                bookname = data["book_name"],
                bookprice = data["price"],
                author = data["author_name"],
                book_type = data["type"]
            )
            return JsonResponse({"status":"success","message":"record inserted successfully"},status = 200)
        return JsonResponse({"status":"pending","message":"only post method is allowed"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"failure","error":f"something went wronng {str(e)}"})
  
#   GET
@csrf_exempt  
def getBookDetails(request):
    try:
        if request.method == 'GET':
            result = list(BookDetails.objects.values())
            if len(result) == 0:
                msg = "no records found"
            else:
                msg = "data retrived successfully"
            return JsonResponse({"status":"success","message":msg,"data":result},status = 200)
        return JsonResponse({"status":"pending","message":"only get method is used"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"failure","msg":"something went wrong","error":str(e)},status = 500)
 
 #PUT 
@csrf_exempt
def updateBookDetails(request,ref_id):
    try:
        if request.method == 'PUT':
            input_data = json.loads(request.body)
            new_price = input_data["new_price"]
            update = BookDetails.objects.filter(id = ref_id).update(bookprice = new_price)
            if update == 0:
                msg = 'no records found with that reference id'
            else:
                msg = 'record updated successfully'
            return JsonResponse({"status":"success","msg":msg},status = 200)
        return JsonResponse({"status":"pending","msg":"only put method allowed"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"failure","msg":"something went wrong","error":str(e)},status = 500)
    
    
@csrf_exempt
def deleteBookDetails(request,ref_id):
    try:
        if request.method == 'DELETE':
            delete_data = BookDetails.objects.filter(id=ref_id).delete()
            if delete_data[0] == 0:
                msg = "no records found"
            else:
                msg = "record deleted successfully"
            return JsonResponse({"status":"success","msg":msg},status = 200)
        return JsonResponse({"status":"pending","msg":"only delete method is used"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"failure","msg":"womething went wrong"},status = 500)