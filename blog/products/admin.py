from django.contrib import admin
from .models import Productmodel
# Register your models here.
@admin.register(Productmodel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['name','weight','price','created_at','updated_at']
    search_fields=('name',)
    list_filter=('price',)