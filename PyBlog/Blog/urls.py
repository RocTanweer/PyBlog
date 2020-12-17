from django.urls import path
from . import views


#When blog/ is entered after the website url, django is referring to this app url (blog.urls) and 
#with empty string, it refers to views.home funciton with a get request and receivce a HttpResponse 
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]