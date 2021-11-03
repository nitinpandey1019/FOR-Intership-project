from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Productmodel(models.Model):
    name=models.CharField(max_length=200)
    weight=models.IntegerField()
    price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)