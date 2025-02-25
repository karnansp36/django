from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Signup_view, name='signup'),
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name= 'login'),
    path('logout/', views.logout_view, name= 'logout'),
]