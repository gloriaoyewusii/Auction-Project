from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import MinLengthValidator, EmailValidator
from django.db import models

class UserModel(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, validators=[EmailValidator])
    password = models.CharField(max_length=255, validators=[MinLengthValidator(8)])

    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    # objects = models.Manager()

# Create your models here.
