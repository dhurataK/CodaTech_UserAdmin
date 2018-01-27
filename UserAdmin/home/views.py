from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
# from .models import Profile
# from .forms import UserForm,ProfileForm
@login_required
def Home(request):
    return render(request, 'home/home.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def new(request):
    return render(request, 'home/new.html')

def create(request):
    return render(request, 'home/home.html')

def show(request, id):
    return render(request, 'home/show.html')

def edit(request,id):
    return render(request, 'home/edit.html')

def update(request):
    print("Update method clicked")
    return render(request, 'home/home.html')

def delete(request,id):
    print("Delete method clicked")
    return render(request, 'home/home.html')
