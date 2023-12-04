from datetime import datetime
import os
import json
import random
import string

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse
from wsgiref.util import FileWrapper
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django_htmx.http import trigger_client_event

from core.settings import MEDIA_URL, BASE_DIR

from . import models
from . import forms
from . import tasks
from . import chatgpt


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    context = {}
    return render(request, 'tinysegment/index.html', context)


@login_required
def dashboard(request):
    context = {}
    return render(request, 'tinysegment/dashboard.html', context)


class CodeComponentListView(ListView):
    model = models.CodeComponent
    template_name = 'tinysegment/codecomponent_list.html'
    context_object_name = 'components'
    ordering = '-id'


class CodeComponentCreateView(CreateView):
    model = models.CodeComponent
    form_class = forms.CodeComponentForm
    template_name = 'tinysegment/codecomponent_form.html'
    success_url = '/codecomponents'


class CodeComponentEditView(UpdateView):
    model = models.CodeComponent
    form_class = forms.CodeComponentForm
    template_name = 'tinysegment/codecomponent_form.html'
    success_url = '/codecomponents'


@login_required
def profile_settings(request):
    context = {}
    return render(request, 'tinysegment/profile_settings.html', context)

@login_required
def aws_s3(request):
    context = {'segment_objects': models.SegmentObjects.objects.all() }
    return render(request, 'tinysegment/aws_s3.html', context)


@login_required
def rest_api(request):
    context = {}
    return render(request, 'tinysegment/rest_api.html', context)


@login_required
def segment_settings(request):
    context = {}
    return render(request, 'tinysegment/segment_settings.html', context)


def registerUser(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = forms.RegistrationForm()
    
    context = {'form': form}
    return render(request, 'tinysegment/register.html', context)


def favicon_ico(request):
    favicon_path = os.path.join(settings.BASE_DIR, 'static', 'favicon.ico')
    return serve(request, os.path.basename(favicon_path), os.path.dirname(favicon_path))


def loginUser(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, "Email OR password is incorrect.")
    else:
        form = forms.LoginForm()
    
    context = {'form': form}
    return render(request, 'tinysegment/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')