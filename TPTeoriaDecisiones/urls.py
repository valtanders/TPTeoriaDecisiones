"""TPTeoriaDecisiones URL Configuration

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

urlpatterns = [
    url(r'^$', 'TeoriaDeDecisiones.views.index', name='index'),
    url(r'^login$', 'TeoriaDeDecisiones.views.user_login', name='login'),
    url(r'^registrar$', 'TeoriaDeDecisiones.views.nuevo_usuario', name='registrar'),
    url(r'^redirect$', 'TeoriaDeDecisiones.views.redirect_registro', name='redirect'),
    url(r'^logout$', 'TeoriaDeDecisiones.views.user_logout', name='logout'),
    url(r'^principal$', 'TeoriaDeDecisiones.views.redirect_principal', name='principal'),
    url(r'^admin', include(admin.site.urls)),
]
