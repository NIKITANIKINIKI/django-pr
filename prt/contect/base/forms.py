from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from base.models import Person, UserComment


class RegisterForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Ваш имя'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Ваш email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Придумайте пароль'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))
    class Meta:
        model=User
        fields=('username','email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Ваш имя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Придумайте пароль'}))

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Ваше имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите Ваш email'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите Ваши комментарии'}))
    captcha = CaptchaField()

class AddForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=['name','content','photo', 'is_pub']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите Ваше имя'}),
            'content': forms.Textarea(attrs={'class': 'form-control','placeholder':'Расскажите о себе','cols': 30, 'rows': 10}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'is_pub': forms.CheckboxInput(attrs={'class':'form-check-input'}), # !!!
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=UserComment
        fields=['user_content']
        widgets={
            'user_content':forms.Textarea(attrs={'class': 'form-input', 'cols': 60, 'rows': 10}),
        }
