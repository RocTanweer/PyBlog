from django.http import request
from django.shortcuts import render 
from .models import Post
from django.contrib.auth.models import User
# from django.http import HttpResponse
# I am going to use render rather than HttpResponse now!


# importing HTTPresponse to give the response to the request made through url
#Creating a view for the home of this blog app.
#taking requests argument because it will accept request through the url
# def home(requests):
#     return HttpResponse('<h1> Hello World </h1>')


#Some Dummy Data for now!

# posts = [
#     {
#         'author' : 'roc_tanweer',
#         'date_posted' : '19-12-2020',
#         'title' : 'Blog-1',
#         'content' : 'This is the first blog'
#     },

#     {
#          'author' : 'roc_tanweer',
#         'date_posted' : '20-12-2020',
#         'title' : 'Blog-2',
#         'content' : 'This is the second blog'
#     },

#     {
#          'author' : 'roc_tanweer',
#         'date_posted' : '21-12-2020',
#         'title' : 'Blog-3',
#         'content' : 'This is the third blog'
#     }
# ]




def home(requests):
    context = {
        'posts' : Post.objects.all()
    }
    return render(requests, 'Blog/home.html', context)


def about(requests):
    return render(requests, 'Blog/about.html', {'title' : 'About'})
