"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from basic.views import home,about,navbar,contact,sample,sample1,sample2,sample3,product,filteringData,filterStudentsByCity,pagination,createData,createProduct,createEmployee,createProductDetails,carPrices,orderPlacing
from basic.views import movieTickets,getOrders,getStudentById,postBookDetails,getbookInfo,courseRegister,getRegisterDetails


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('navbar/',navbar,name='navbar'),
    path('sample/',sample),
    path('sample1/',sample1),
    path('sample2/',sample2),
    path('sample3/',sample3),
    path('product/',product),
    path('filter/',filteringData),
    path('students/',filterStudentsByCity),
    path('pagination/',pagination),
    path('create/',createData),
    path('createproduct/',createProduct),
    path('empdetails/',createEmployee),
    path('productdetails/',createProductDetails),
    path('prices/',carPrices),
    path('order/',orderPlacing),
    path('ticket/',movieTickets),
    path('orderDetails/',getOrders),
    path('studentData/<int:id>',getStudentById),
    path('bookinfo/',postBookDetails),
    path('getbookinfo/',getbookInfo),
    path('courseReg/',courseRegister),
    path('getReg/',getRegisterDetails)
]
