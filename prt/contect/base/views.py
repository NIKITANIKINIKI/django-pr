from urllib import request

from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, DetailView
from django.contrib.auth.decorators import login_required


from .forms import RegisterForm, ContactForm, AddForm
from .models import *


menu=[{'title':"Поиск", 'url_name':'home'},
      {'title':'ОБРАТНАЯ СВЯЗЬ', 'url_name':'feedback'},
      {'title':'ДОБАВИТЬ АНКЕТУ', 'url_name':'add'},
      {'title':'ВОЙТИ', 'url_name':'login'},
      {'title':'РЕГИСТРАЦИЯ', 'url_name':'register'}]


class Home(ListView):
    model=Person
    template_name = 'base/base.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['menu']=menu
        context['title']='Главная страница'
        return context

    def get_queryset(self):
        return Person.objects.order_by('?')[:3]


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

class Register(CreateView):
    form_class=RegisterForm
    template_name='base/register.html'
    success_url=reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['menu']=menu
        context['title']='Регистрация'
        return context

class Login(LoginView):
    form_class=AuthenticationForm
    template_name='base/register.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['menu']=menu
        context['title']='Вход'
        return context
    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')

class FeedbackForm(FormView):
    form_class=ContactForm
    template_name='base/register.html'
    success_url=reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['menu']=menu
        context['title']='Обратная связь'
        return context
    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

class PostDetailView(DetailView):
    model = Person
    template_name = 'base/objects.html'
    context_object_name = 'person'
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['menu']=menu
        context['title']='Персонаж'
        return context


class AddContent(CreateView):
    form_class=AddForm
    template_name='base/register.html'
    context_object_name = 'person'
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['menu']=menu
        context['title']='Добавление статьи'
        context['enctype'] = 'multipart/form-data'
        return context
    def get_success_url(self):
        return reverse_lazy('home')