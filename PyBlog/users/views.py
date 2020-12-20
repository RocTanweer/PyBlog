from django import forms
from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
#Now importing forms.py that I created by inheriting UserCreationFrom and using django.forms
#to add an extra Email field in registration form
from .forms import UserRegisterForm
from django.contrib import messages




def register(request):
    #If there is a post request from registration form---------
    if request.method == 'POST':
        #Now we wiil get a form with all data entered in the form through post request
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        #Checking if the data filled is valid after a post request
        if form.is_valid():
            #if it is valid, saving it!
            form.save()
            #Usercreation_obj.cleaned_data is a dictionary with all the fields as key and their as value
            #Like this, we can retrieve any data from the UserCreationForm!
            username = form.cleaned_data.get('username')
            #making a notification/alert for the same
            messages.success(request, f'Account for {username} has been created!')
            #redirecting after creating the user to blog-home.
            #if not do so, Account will be created and we will also get respective information but 
            #we will be redirected to the same registration page with our registered data filled!
            return redirect('blog-home')

    #If there is a get request!
    else:
        #getting an empty form through a get request
        # form = UserCreationForm()
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form' : form})






def profile(request):
    return render(request, 'users/profile.html')