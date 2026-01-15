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
from basic.views import add_User, add_student, average_percentage, engineeringSeat, filter_users, get_all_users, home,about, job1,navbar,contact, pass_vs_fail,sample,sample1,sample2,sample3,product,filteringData,filterStudentsByCity,pagination,createData,createProduct,createEmployee,createProductDetails,carPrices,orderPlacing, signup, soft_delete_student, students_with_grade_a, top_3_students
from basic.views import deleteBookDetails,updateBookDetails,getBookDetails,postBookDetails,updataUserByStatus,deleteUserDataById,updateUserageById,updateUserById,updateMovieScreen,getMovieByMultipleScreens,getMovieByScreenname,getMovieByGenres,getMovieDetails,movieTickets,getOrders,getStudentById,postBookDetails,getbookInfo,courseRegister,getRegisterDetails,getStudentByDegree,getOrdersByStatus


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
    path('getmovie/',getMovieDetails),
    path('movieByGenres/<str:genres_val>', getMovieByGenres),
    path('getByScreenname/<str:screen_name>',getMovieByScreenname),
    path('getBymultipleScreens/<str:first>/<str:second>',getMovieByMultipleScreens),
    path('orderDetails/',getOrders),
    path('studentData/<int:id>',getStudentById),
    path('bookinfo/',postBookDetails),
    path('getbookinfo/',getbookInfo),
    path('courseReg/',courseRegister),
    path('getReg/',getRegisterDetails),
    path('getStudentsByDegree/<str:deg>',getStudentByDegree),
    path('orderBystatus/<str:status_param>',getOrdersByStatus),
    path('updateScreen/<str:screen_name>/',updateMovieScreen),
    path('updateCity/',updateUserById),
    path('updateAge/',updateUserageById),
    path('deleteUser/<int:ref_id>',deleteUserDataById),
    path('updateStatus/<str:ref_status>/',updataUserByStatus),
    path('bookDetails/',postBookDetails),
    path('getDetails/',getBookDetails),
    path('updatePrice/<int:ref_id>/',updateBookDetails),
    path('deleteBookDetails/<int:ref_id>/',deleteBookDetails),
    path('job1/',job1),
    path('engineeringSeat/',engineeringSeat),
    path('signup/',signup),
    path('add_user/',add_User),
    path('get_users/',get_all_users),
    path('users/filter/',filter_users),
    path('add-student/',add_student),
    path('grade-a/',students_with_grade_a),
    path('top-3/',top_3_students),
    path('average/',average_percentage),
    path('pass-fail/',pass_vs_fail),
    path('delete/<int:student_id>/',soft_delete_student)
]
