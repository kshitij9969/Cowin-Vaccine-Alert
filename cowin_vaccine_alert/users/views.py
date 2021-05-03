from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

from .forms import CreateUserForm

# Create your views here.


class CreateUserView(CreateView):
    """
    View to create user accounts.
    """
    model = User
    fields = ['first_name', 'last_name', 'email', 'password']
    form_class = CreateUserForm


