from django.urls import path
from .views import *

urlpatterns = [
    path('', trainee_list, name='trainee_list'),
    path('add/', add_trainee, name='add_trainee'),
    path('update/<int:id>/', update_trainee, name='update_trainee'),
    path('delete/<int:trainee_id>/', delete_trainee, name='delete_trainee'),
]
