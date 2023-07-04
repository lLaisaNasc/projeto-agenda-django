from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    #---- id é feito de forma automatica -------

    first_name = models.CharField(max_length=50)
    #campo opcional
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    #campo opcional
    email = models.EmailField(max_length=254, blank=True)
    #data atual de forma automática
    created_date = models.DateTimeField(default=timezone.now)
    #campo opcional
    description = models.TextField(blank=True)