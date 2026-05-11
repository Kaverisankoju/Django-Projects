from django.urls import path
from . import views

urlpatterns = [

    path('', views.job_list, name='job_list'),

    path('home/', views.home, name='home'),

    path('add-job/',
         views.add_job,
         name='add_job'),

    path('apply/<int:job_id>/',
         views.apply_job,
         name='apply_job'),

    path('my-applications/',
         views.my_applications,
         name='my_applications'),
    
    path(
    'delete-application/<int:app_id>/',
    views.delete_application,
    name='delete_application'
),

]