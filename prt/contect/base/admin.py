from django.contrib import admin

# Register your models here.
from .models import *

class BaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time','is_pub')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')


admin.site.register(Person, BaseAdmin)