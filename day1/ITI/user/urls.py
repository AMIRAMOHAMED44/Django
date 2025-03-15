from django.urls import path
# from .views import registerview
from django.contrib.auth.views import LoginView , LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
