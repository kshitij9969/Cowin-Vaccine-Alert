from django.forms import ModelForm
# from django.contrib.auth.models import User

from .models import User, Alert


class CreateUserForm(ModelForm):
     class Meta:
         model = User
         fields = ['first_name', 'last_name', 'email', 'password']


class CreateAlertForm(ModelForm):
    class Meta:
        model = Alert
        fields = ['age_group', 'state', 'region']
