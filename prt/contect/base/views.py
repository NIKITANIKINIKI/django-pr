from urllib import request
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, DetailView
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm, ContactForm, AddForm, CommentForm, LoginForm
from .models import *
from django.contrib.auth import login

class Home(MyMixin,ListView):
    model=Person
    paginate_by=3
    template_name = 'base/content.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context_m=self.get_user_context(title='Главная страница')
        context=dict(list(context.items())+list(context_m.items()))
        return context

    def get_queryset(self):
        return Person.objects.filter(is_pub=True)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

class Register(MyMixin,CreateView):
    form_class=RegisterForm
    template_name='base/register.html'
    success_url=reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context_m = self.get_user_context(title='Добро пожаловать!')
        context = dict(list(context.items()) + list(context_m.items()))
        return context

    def form_valid(self, form):
        user=form.save()
        login(self.request, user)
        return redirect('home')

class Login(MyMixin,LoginView):
    form_class=LoginForm
    template_name='base/register.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context_m = self.get_user_context(title='Давно не виделись!')
        context = dict(list(context.items()) + list(context_m.items()))
        return context
    def get_success_url(self):
        return reverse_lazy('add')


def logout_user(request):
    logout(request)
    return redirect('home')

class FeedbackForm(MyMixin,FormView):
    form_class=ContactForm
    template_name='base/register.html'
    success_url=reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context_m = self.get_user_context(title='Обратная связь')
        context = dict(list(context.items()) + list(context_m.items()))
        return context
    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

class PostDetailView(LoginRequiredMixin,MyMixin,DetailView):
    model = Person
    template_name = 'base/objects.html'
    context_object_name = 'person'
    login_url = reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context_m = self.get_user_context(title='Соискатели')
        context = dict(list(context.items()) + list(context_m.items()))
        person=self.get_object()
        comments=UserComment.objects.filter(person=person).order_by('created_time')
        form=CommentForm()
        context['comments']=comments
        context['form']=form
        return context

    def post(self, request, *args, **kwargs):
        person=self.get_object()
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.user=request.user #привязываем пользователя к текущему коммментарию
            comment.person=person
            comment.save()
            return redirect('post_detail', pk=person.id)
        else:
            context=self.get_context_data(**kwargs)
            context['form']=form
            return render(request, self.template_name, context)


class AddContent(LoginRequiredMixin,CreateView):
    form_class=AddForm
    template_name='base/register.html'
    context_object_name = 'person'
    login_url=reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['menu']=menu
        context['title']='Добавить анкету'
        context['enctype'] = 'multipart/form-data'
        return context
    def get_success_url(self):
        return reverse_lazy('home')

class MyCategory(MyMixin,ListView):
    model=Person
    paginate_by=3
    template_name = 'base/content.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context_m=self.get_user_context(title='Главная страница')
        context=dict(list(context.items())+list(context_m.items()))
        context['cats'] = Category.objects.all()
        return context

    def get_queryset(self):
        cat_id = self.kwargs.get('cat_id')
        return Person.objects.filter(cat_id=cat_id,is_pub=True)