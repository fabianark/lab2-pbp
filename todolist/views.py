from datetime import date
from random import randint
from telnetlib import STATUS
from urllib import response
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from todolist.models import Task
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import AnonymousUser

# Create your views here.

def register_account(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!')
            return redirect('todolist:user_login')
    
    context = {'form':form}
    return render(request, 'register_account.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:show_todolist'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Wrong username or password!')

    context = {}
    return render(request, 'user_login.html', context)

def user_logout(request):
    logout(request)
    return redirect('todolist:user_login')

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user.username

    context = {
        'todolist': Task.objects.filter(user=request.user),
        'username': username,
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task(user=user, date=date.today(), title=title, description=description)
        task.save()

        messages.success(request, 'A task has been added!')
        return redirect('todolist:show_todolist')
    
    context = {}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def change_status(request):
    task = Task.objects.get(pk=request.POST['pk'])
    task.is_finished = not task.is_finished
    task.save()

    messages.success(request, 'A task status has been changed!')
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete_task(request):
    task = Task.objects.get(pk=request.POST['pk'])
    task.delete()

    messages.success(request, 'A task has been deleted!')
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def show_json(request):
    data = Task.objects.filter(user=request.user.id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
def add_task_ajax(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task(user=user, date=date.today(), title=title, description=description)
        task.save()

        return HttpResponse("Task: " + title + " have been added")

    return HttpResponse(status=400)

@login_required(login_url='/todolist/login/')
def delete_task_ajax(request, id):
    task = Task.objects.get(pk=id)
    title = task.title
    task.delete()

    return HttpResponse("Task: " + title + " have been deleted")