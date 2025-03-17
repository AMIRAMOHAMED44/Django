from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView , LogoutView
from .views import custom_logout


urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', custom_logout, name='logout'),
    path('register/', register, name='register'),

]

