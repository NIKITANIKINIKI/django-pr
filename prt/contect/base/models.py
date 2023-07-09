from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=255, verbose_name='Имя')
    content=models.TextField(max_length=255, verbose_name='Расскажите о себе')
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Добавьте, пожалуйста, Ваше фото')
    time=models.DateTimeField(auto_now_add=True)
    is_pub=models.BooleanField(default=True, verbose_name='Согласны ли Вы сделать ваше фото доступным другим пользователям?')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Соискатели'
        verbose_name_plural='Соискатели'
        ordering=['time', 'name']

class Activite(models.Model):
    pass