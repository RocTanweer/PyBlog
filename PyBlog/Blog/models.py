from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#Creating a class by inheriting Model class in models
#This is the structure of a table in the database in the form of a class
#We will make different fields for that table as a class attributes

class Post(models.Model):
    #This is for title field of our Post with max lenght of 100 words.
    title = models.CharField(max_length=100)
    #This is for our post content field with no word limit.
    content = models.TextField()
    #We could use 'auto_now' or 'auto_now_add' but we used 'default=timezone.now' so we can edit date/time of posts.
    date_posted = models.DateTimeField(default=timezone.now)
    #This means one-to-many relationship,on_delete is to ensure when users is deleted,their posts as well be deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    #We will make str of this class,so when an object of post model is printed,django will show their title.
    def __str__(self):
        return f'Title is {self.title}'


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={ 'pk' : self.pk })

