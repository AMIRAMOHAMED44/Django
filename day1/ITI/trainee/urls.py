from django.urls import path
from .views import trainee_list, add_trainee, update_trainee, delete_trainee

urlpatterns = [
    path('', trainee_list, name='trainee_list'),
    path('add/', add_trainee, name='add_trainee'),
    path('update/<int:trainee_id>/', update_trainee, name='update_trainee'),
    path('delete/<int:trainee_id>/', delete_trainee, name='delete_trainee'),
]
