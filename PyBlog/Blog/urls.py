from django.urls import path
from . import views


#When blog/ is entered after the website url, django is referring to this app url (blog.urls) and 
#with empty string, it refers to views.home funciton with a get request and receivce a HttpResponse 
urlpatterns = [
    #Using function based view for blog-home
    # path('', views.home, name='blog-home'),
    #using class based view for blog-home
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
]