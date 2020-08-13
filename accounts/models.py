from django.db import models
from django.contrib.auth.models import User

class UserForm(User):
    email = models.EmailField(primary_key=True,unique=True),
    ID = models.CharField(max_length=3, primary_key=True)
 