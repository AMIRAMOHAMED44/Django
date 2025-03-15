from django.urls import path
from .views import *

urlpatterns = [
    # path('', course_list, name='course_list'),
    # path('add/', add_course, name='add_course'),
    path('', ListCourse.as_view(), name='course_list'),
    path('add/',AddCourse.as_view(), name='add_course'),
    path('update/<int:pk>/', UpdateCourse.as_view(), name='update_course'),
    # path('update/<int:id>/', update_course, name='update_course'),
    path('delete/<int:id>/', delete_course, name='delete_course'),
]
