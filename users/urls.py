"""为应用程序users定义URL模式"""

from django.contrib.auth.views import LoginView
from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$',  views.register, name='register')
]