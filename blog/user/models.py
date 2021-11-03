from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Usermodel(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    def get_email_address(emails):
        try:
            return Usermodel.objects.get(email=emails)
        except:
            return False
    def email_isexits(self):
        return Usermodel.objects.filter(email=self.email)

    def __str__(self):
        return self.first_name

class Postmodel(models.Model):
    user=models.ForeignKey(Usermodel,on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)





