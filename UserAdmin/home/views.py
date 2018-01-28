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
    if request.user.is_authenticated():
        context = {
            'clients': Client.objects.all()
        }
        return render(request, 'home/home.html',context)
    else:
        return HttpResponseRedirect('/')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def new(request):
    if request.user.is_authenticated():
        return render(request, 'home/new.html')
    else:
        return HttpResponseRedirect('/')

def create(request):
    if request.user.is_authenticated():
        if request.POST:
            new_client = Client.objects.create_user(request.POST, admin = request.user)
            if new_client[0]:
                return redirect(reverse('home'))
            else:
                for error in new_client[1]:
                    messages.error(request, error)
                    return redirect(reverse('new_client'))

def show(request, id):
    if request.user.is_authenticated():
        client = Client.objects.get(id=id)
        context = {
            'client': client
        }
        return render(request, 'home/show.html',context)
    else:
        return HttpResponseRedirect('/')

def edit(request,id):
    if request.user.is_authenticated():
        client = Client.objects.get(id=id)
        context = {
            'client': client
        }
        return render(request, 'home/edit.html', context)
    else:
        return HttpResponseRedirect('/')

def update(request):
    if request.user.is_authenticated():
        if request.POST:
            client_id = request.POST['id']
            client = Client.objects.get(id=client_id)
            if request.user.id == client.admin.id:
                updated_client = Client.objects.update_client(request.POST)
                if updated_client[0]:
                    return redirect(reverse('home'))
                else:
                    for error in updated_client[1]:
                        messages.error(request, error)
            return redirect('/edit/' + str(request.POST['id']))

def delete(request,id):
    if request.user.is_authenticated():
        client = Client.objects.get(id=id)
        if request.user.id == client.admin.id:
            Client.objects.get(id=id).delete()
        return redirect(reverse('home'))
