from django.urls import path
from .views import AddCourseView, course_list, UpdateCourseView

urlpatterns = [
    path('courses/', course_list, name='course-list'),
    path('courses/add/', AddCourseView.as_view(), name='add-course'),
    path('courses/update/<int:id>/', UpdateCourseView.as_view(), name='course-update'),
]
