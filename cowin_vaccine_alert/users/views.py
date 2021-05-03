from django.shortcuts import render
# from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth import login

from django.shortcuts import redirect

from .forms import CreateUserForm, CreateAlertForm
from .models import Alert, User

# Create your views here.


class CreateUserView(CreateView):
    """
    View to create user accounts.
    """
    model = User
    fields = ['first_name', 'last_name', 'email', 'password']
    form_class = CreateUserForm
    success_url = 'login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        alert = Alert()
        self.object.alert = alert
        self.object.save()

        return redirect(self.get_success_url())





class UpdateAlertView(UpdateView):
    """
    View to create alerts
    """
    model = Alert
    fields = ['age_group', 'state', 'region']
    form_class = CreateAlertForm



