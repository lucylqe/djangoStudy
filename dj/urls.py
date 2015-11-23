"""dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from polls import urls as polls_urls
from home import urls as home_urls
urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='home/index.html')),
    # use module
    url(r'^home/',include(home_urls, namespace='home')),
    # use six.string type. will be convert to module using load_module("home.urls")
    url(r'^blog/',include("blog.urls", namespace='blog')),
    url(r'^books/',include("books.urls",namespace='books')),
    url(r'^polls/',include(polls_urls,namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),

]
