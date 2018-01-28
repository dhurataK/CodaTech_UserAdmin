from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import Client
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.urls import reverse

@login_required
def Home(request):
    context = {
        'clients': Client.objects.all(),

    }
    return render(request, 'home/home.html',context)

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def new(request):
    return render(request, 'home/new.html')

def create(request):
    if request.user.is_authenticated():
        if request.POST:
            new_client = Client.objects.create_user(request.POST, admin = request.user)
            if new_client[0]:
                # request.session['user'] = new_client[1]
                return redirect('/')
            else:
                for error in new_client[1]:
                    messages.error(request, error)
                    return redirect(reverse('new_user'))

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
