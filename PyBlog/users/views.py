from django import forms
from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
#Now importing forms.py that I created by inheriting UserCreationFrom and using django.forms
#to add an extra Email field in registration form
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required





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
            return redirect('login')

    #If there is a get request!
    else:
        #getting an empty form through a get request
        # form = UserCreationForm()
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form' : form})





@login_required
def profile(request):
    if request.method == 'POST':
        #request.POST gives the modelform with the post data filled in
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        #request.user gives the current logged in user
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)