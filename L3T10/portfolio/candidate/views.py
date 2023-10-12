from django.shortcuts import render, redirect
from .models import BlogPost
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def homepage(request):
    '''
    Renders the homepage.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template for the homepage.
    '''
    return render(request, 'candidate/homepage.html')

@login_required()
def blog(request):
    '''
    Renders the blog page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template for the blog page with blog posts.
    '''
    posts = BlogPost.objects.all().order_by('-pub_date')
    return render(request, 'candidate/blog.html', {'posts': posts})

def contact(request):
    '''Renders the contact page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template for the contact page.'''
    return render(request, 'candidate/contact.html')

def signup(request):
    '''Handles user registration.

    If the HTTP request method is POST, it processes the user registration form. If the form is valid,
    the user is registered, logged in, and redirected to the homepage. If the form is not valid,
    it displays the registration form.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered registration form or a redirect to the homepage upon successful registration.
    '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'candidate/signup.html', {'form': form})

def login_view(request):
    '''Handles user login.

    If the HTTP request method is POST, it attempts to authenticate the user based on the provided
    username and password. If authentication is successful, the user is logged in and redirected to
    the homepage. If authentication fails, an error message is displayed.

    Args:
        request: The HTTP request object.

    Returns:
        A redirect to the homepage upon successful login or an error message on failed login.
  '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Incorrect username or password. Please try again.')

    return render(request, 'registration/login.html')