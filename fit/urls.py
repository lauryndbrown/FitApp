from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'^index', views.index, name='home'),
		url(r'^about', views.about, name='about'),
        url(r'^game', views.character, name='game'),
		url(r'^character', views.character, name='character'),
		url(r'^shop', views.shop, name='shop'),
		url(r'^adventure', views.adventure, name='adventure'),
        url(r'register/$', views.register, name='register'),
]
