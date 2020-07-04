from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.


def index(request):
    return render(request, 'login/index.html')


def validate(request):
    user_name = request.POST['username']
    password = request.POST['password']
    result = User.objects.login_user(
        name=user_name, password=password)
    return render(request, 'login/validate.html', {'username': user_name, 'password': password, "result": result})


def register(request):
    return render(request, 'login/register.html')


def adduser(request):
    new_user = request.POST['newuser']
    new_password = request.POST['newpassword']
    confirm_password = request.POST['confirmpassword']
    result = User.objects.create_user(
        name=new_user, password=new_password, confirm_password=confirm_password)
    return render(request, 'login/adduser.html', {'newuser': new_user, 'newpassword': new_password, "result": result[0], "match": result[1]})
