from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from base.models import Person

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username', 'password1', 'password2')
        widgets={
            'username': forms.TextInput(attrs={'class':'form-input'}),
            'password1': forms.PasswordInput(attrs={'class':'form-input'}),
            'password2': forms.PasswordInput(attrs={'class':'form-input'}),
        }

class ContactForm(forms.Form):
    name=forms.CharField(label='Имя', max_length=255 )
    email=forms.EmailField(label='Email')
    content=forms.CharField(label='Комментарии', widget=forms.Textarea(attrs={'cols':60, 'rows':10}))
    captcha=CaptchaField(label='Введите пожалуйста текст с картинки')

class AddForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=['name','content','photo', 'is_pub']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'class': 'form-input', 'cols': 60, 'rows': 10}),
            'photo': forms.FileInput(attrs={'class': 'form-input'}),
            'is_pub': forms.CheckboxInput(attrs={'class': 'form-input'}),
        }