import uuid
from django.db import models

# Create your models here.
class userProfile(models.Model):
    name = models.CharField(max_length = 150)
    age = models.IntegerField() 
    city = models.CharField(max_length = 150)
    
class Employee(models.Model):
    emp_name = models.CharField(max_length=150)
    emp_salary = models.IntegerField()
    emp_email = models.EmailField(unique=True)
    
class ProductDetails(models.Model):
    prod_name = models.CharField(max_length=150)
    prod_price = models.IntegerField()
    prod_quantity = models.IntegerField()
    total_price = models.IntegerField()
    
    def save(self,*args,**kwargs):
        self.total_price = self.prod_price * self.prod_quantity
        super().save(*args,**kwargs)
    
class OrderDetails(models.Model):
    useremail = models.EmailField(unique=True)
    orderid = models.CharField(max_length=100,unique=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    mode = models.CharField(max_length=50)
    status = models.CharField(max_length=80)
    dateandtime = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(default="INR",max_length=50)
    transaction_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    
class MovieTicketBooking(models.Model):
    moviename = models.CharField(max_length=150)
    genres = models.CharField(max_length=100,default="Action")
    showtime = models.DecimalField(max_digits=10,decimal_places=2)
    screenname = models.CharField(max_length=150)
    dataandtime = models.DateTimeField(auto_now_add=True)
    trasactionid = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    genres = models.CharField(max_length=100,default="Action")
    
    
    
class BookInfo(models.Model):
    bookname = models.CharField(max_length=100)
    authorName = models.CharField(max_length=100)
    category = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    rating = models.DecimalField(max_digits=5,decimal_places=1)
    
class CourseRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    registered = models.DateTimeField(auto_now_add=True)
    
  
class BookDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    bookname = models.CharField(max_length=100)
    bookprice = models.IntegerField()
    author = models.CharField(max_length=100)
    book_type = models.CharField(max_length=100)  