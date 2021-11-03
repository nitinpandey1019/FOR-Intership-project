from django.shortcuts import render
from django.views import View
from .models import Usermodel,Postmodel
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login,login
from .forms import LogInForm
# Create your views here.
def user(request):
    return render(request,'user/user.html')
def about(request):
    return render(request,'user/about.html')
class Signup(View):
    def get(self,request):
        return render(request, 'user/signup.html')
    def post(self,request):
        if request.method=='POST':
            postdata = request.POST
            first_name = postdata.get('fname')
            last_name = postdata.get('lname')
            username = postdata.get('uname')
            email = postdata.get('email')
            password = postdata.get('password')
            values={
                'first_name':first_name,
                'last_name':last_name,
                'username':username,
                'email':email,
                'password':password,
            }
            userdata=Usermodel(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            error_messages=self.validation(userdata)

            if error_messages:
                data={
                'error':error_messages,
                'value':values,
                }
                return render(request,'user/signup.html',data)
            else:
                userdata.password=make_password(userdata.password)
                userdata.save()
                return HttpResponseRedirect("/")
        else:
            return HttpResponse("Data is not saved")
    def validation(self,userdata):
        error_messages = None
        if not userdata.first_name:
            error_messages = 'Insert FirstName'
        elif len(userdata.first_name) < 4:
            error_messages = 'firstname smaller than 4 character'
        elif not userdata.last_name:
            error_messages = 'Insert LastName'
        elif len(userdata.last_name) < 4:
            error_messages = 'Lastname smaller than 4 character'
        elif not userdata.username:
            error_messages = 'Enter the username'
        elif not userdata.email:
            error_messages = 'Enter the email'
        elif not userdata.password:
            error_messages = 'Enter the password'
        elif userdata.email_isexits():
             error_messages='Email already already registerd..'
        return error_messages
# Login area
class Login(View):
    def get(self,request):
        return render(request,'user/login.html')
    def post(self,request):
        post=request.POST;
        userdata=Usermodel()
        emails=post.get('email')
        password=post.get('password')
        values={
            'email':emails,
            'password':password,
        }
        useremail=Usermodel.get_email_address(emails)
        error_messages=None
        if useremail:
            flag = check_password(password,useremail.password)
            if flag:
                request.session['uemail']=request.POST['email']
                return HttpResponseRedirect('/profile/')
            else:
                error_messages = "Your Email and Password is Incorrect"
        else:
            error_messages = "Your Email address is not valid"
        data={
            'error':error_messages,
            'value':values,
        }
        return render(request, 'user/login.html',data)


def post(request):
    data=Postmodel.objects.all()
    print(data)
    return render(request,'user/home.html',{'data':data})

def profile(request):
    if request.session.has_key('uemail'):
        p = Postmodel.objects.all()
        return render(request,'user/profile.html',{'data':p})
    else:
        return HttpResponseRedirect('/user/login/')
def logout(request):
    del request.session['uemail']
    return HttpResponseRedirect('/')

