from django.contrib import admin
from .models import Usermodel,Postmodel
# Register your models here.
@admin.register(Usermodel)
class UserModelAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','username','email','password']

@admin.register(Postmodel)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['user','text','created_at','updated_at']
