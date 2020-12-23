from django.http import request
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
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
    paginate_by = 10
    ordering = ['-date_posted']

class UserPostListView(ListView):
    #specifying the model whose objects are listed in listView
    model = Post
    #default context_object_name is 'object_list'
    context_object_name = 'posts'
    #default is 'app/model_list.html'
    template_name = 'Blog/user_posts.html'
    paginate_by = 5
    ordering = ['-date_posted']


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)



class PostDetailView(DetailView):
    #specifying the model whose object are showed in detail view
    model = Post
    #here 
    #template name is default,Blog/post_detail.html
    #and
    #object_context_name is also default to object 


#LoginRequiredMixin is just like the decorator we used for profile view function
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'Blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.info(self.request, f'Your post "{form.instance.title}" has been posted successfully!')
        return super().form_valid(form)


   
#LoginRequiredMixin is just like the decorator we used for profile view function
"""
Reason for using UserPassesTestMixin even though we have used LoginRequiredMixin:
If you are logged out of your blog account and try to write the url for like deleting a post, you will certainly get
redirected to login page.But the downfall is that if you are writing a url to delete/update a post that belongs 
to someone else, You will still be able to do so(which is obviously absurd).That is why we used UserPassesTestMixin.
Now if you try to delete/update a post of someone else, you will get redirected to login page first,but if you do not
enter the credentials of that user,it will throw a '403 Forbidden'
"""
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'Blog/post_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.info(self.request, f'Your post "{form.instance.title}" has been updated successfully!')
        return super().form_valid(form)

    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#LoginRequiredMixin is just like the decorator we used for profile view function
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Post    
    success_url = '/'
    template_name = 'Blog/post_delete.html'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




def about(requests):
    return render(requests, 'Blog/about.html', {'title' : 'About'})
