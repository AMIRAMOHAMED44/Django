from django.urls import path,include
from .views import *

urlpatterns = [

    # path('', ListCourse, name='course_list'),
    # path('add/',AddCourse, name='add_course'),
    # path('update/<int:pk>/', UpdateCourse, name='update_course'),
    # path('delete/<int:pk>/', DeleteCourse, name='delete_course'),

    # path('', course_list, name='course_list'),
    #  path('add/', add_course, name='add_course'),
    #  path('update/<int:id>/', update_course, name='update_course'),
    # path('delete/<int:id>/', delete_course, name='delete_course'),

    #rest framework
      path('api/', include('course.api.urls')),



]




