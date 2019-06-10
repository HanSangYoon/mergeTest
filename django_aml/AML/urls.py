"""django_AML URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from AML import views

app_name = 'aml'

urlpatterns = [
    path('', views.home, name='home'),
    path('f_crawling/', views.f_crawling, name='f_crawling'),
    path('i_crawling/', views.i_crawling, name='i_crawling'),
    path('t_crawling/', views.t_crawling, name='t_crawling'),
    path('y_crawling/', views.y_crawling, name='y_crawling'),
    path('g_crawling/', views.g_crawling, name='g_crawling'),
]
