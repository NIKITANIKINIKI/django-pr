from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(),name='login'),
    path('logout/', logout_user, name='logout'),
    path('contact/', FeedbackForm.as_view(), name='feedback'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]