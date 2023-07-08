from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class RegisterForm(UserCreationForm):
    # username=forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    # password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
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

# class AddForm(forms.Form):
#     name = forms.CharField(max_length=255)
#     content = forms.CharField(max_length=255)
#     photo = forms.ImageField(upload_to='photos/%Y/%m/%d/')
#     time = forms.DateTimeField(auto_now_add=True)
#     is_pub = forms.BooleanField(default=True)