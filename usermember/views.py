from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class RegisterUser(View):
    def get(self, request):
        rf = RegisterForm
        return render(request, 'usermember/register.html', {"rf": rf})
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.save()

        return HttpResponse ("Dang ky thanh cong")

class LoginUser(View):
    def get(self, request):
        lf = LoginForm
        return render (request, 'usermember/login.html', {"lf": lf})
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username = User.objects.get(email = username), password = password)
        except:
            user = authenticate(request, username = username, password = password)
            
        if user is not None:
            login(request, user)
            return render (request, 'usermember/private.html')
        else:
            return HttpResponse ("Login fail")

def LogoutUser(request):
    logout(request)
    return HttpResponse ("Log out")

# @login_required(login_url='/login')

class privatepage(LoginRequiredMixin, View):
    login_url='/login/'
    def get(request):
        return render (request, 'usermember/private.html')