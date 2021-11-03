from django.contrib import admin
from django.urls import path
from user import views
from user.views import Signup,Login
from products.views import Products
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.post,name='post'),
    path('user/',views.user,name='user'),
    path('user/signup/',Signup.as_view(),name='signup'),
    path('user/login/',Login.as_view(),name='login'),
    path('about/',views.about,name='about'),
    path('products/', Products.as_view(), name='products'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout,name='logout'),
]
