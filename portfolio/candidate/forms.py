from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    '''Custom form for user registration.

    Inherits from UserCreationForm to provide user registration functionality.

    Attributes:
        Meta (class): A nested class to specify form options.
            - model (str): The model used for user registration (should be 'candidate').
            - fields (list): The fields to display in the registration form.

    Usage:
        Use this form to handle user registration by creating an instance of this class.
   '''
    class Meta:
        model = 'candidate'
        fields = ['username', 'password1', 'password2']
