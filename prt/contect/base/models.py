from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=255)
    content=models.TextField(max_length=255)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/')
    time=models.DateTimeField(auto_now_add=True)
    is_pub=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    def get_absolute(self):
        pass

    class Meta:
        verbose_name='Соискатели'
        verbose_name_plural='Соискатели'
        ordering=['time', 'name']

class Activite(models.Model):
    pass