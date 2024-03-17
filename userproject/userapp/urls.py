
from django.urls import path
from .import views
app_name='us'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('',views.login,name='login'),
    path('home/',views.home,name='home'),
]