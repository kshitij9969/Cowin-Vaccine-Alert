from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin


# Create your models here.

class Alert(models.Model):
    """
    Model for storing alerts
    """
    age_group = models.CharField(max_length=255, default="Age 18 to 44")
    state = models.CharField(max_length=255)
    region = models.CharField(max_length=255)


class UserManager(BaseUserManager):
    """
    Manager model for user
    """
    def create_user(self, full_name, email,
                    password, *args, **kwargs):
        """
        function to create user
        :param dob:
        :param profile_picture: Profile picture of the user
        :param first_name: First name of user
        :param last_name: Last name of user
        :param employee_id: employee id of user
        :param email: email address of user
        :param password: password(hashed)
        :return: User object
        """
        if not all([full_name, email]):
            raise ValueError("Fields missing!")

        email = self.normalize_email(email)
        user = self.model(full_name=full_name,
                          email=email, *args, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    # def create_superuser(self, username, full_name, nick_name,
    #                      email, password, *args, profile_picture=None, **kwargs):
    #     """
    #     Function to create superuser
    #     :param profile_picture: Profile picture of the user
    #     :param first_name: First name of user
    #     :param last_name: Last name of user
    #     :param employee_id: employee id of user
    #     :param email: email address of user
    #     :param password: password(hashed)
    #     :return: User object
    #     """
    #     email = self.normalize_email(email)
    #     user = self.create_user(username=username,
    #                             profile_picture=profile_picture,
    #                             full_name=full_name, nick_name=nick_name, email=email,
    #                             password=password, *args, **kwargs)
    #     user.is_superuser = True
    #     user.save(using=self._db)
    #
    #     return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model for user objects
    """
    """
    Basic information
    """
    email = models.EmailField(max_length=200, unique=False, null=False)
    full_name = models.CharField(max_length=100, unique=False, null=False)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    account_update_date = models.DateField(auto_now=True, null=True, blank=True)
    alert = models.OneToOneField(Alert, on_delete=models.CASCADE)
    """
    Permission information
    """
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    """
    Organization information
    """

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        """
        String representation of User object
        :return: String object
        """
        return f"full_name: {self.full_name}, email: {self.email}"


