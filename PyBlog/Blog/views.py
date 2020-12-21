from django.http import request
from django.shortcuts import render 
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
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



#for iteration, it's 'object_list' by default
#for just using model's object, it's 'object' by default
#for context_object_name
class PostListView(ListView):
    #specifying the model whose objects are listed in listView
    model = Post
    #default context_object_name is 'object_list'
    context_object_name = 'posts'
    #default is 'app/model_list.html'
    template_name = 'Blog/home.html'


class PostDetailView(DetailView):
    #specifying the model whose object are showed in detail view
    model = Post
    #here 
    #template name is default,Blog/post_detail.html
    #and
    #object_context_name is also default to object 
    




def about(requests):
    return render(requests, 'Blog/about.html', {'title' : 'About'})
