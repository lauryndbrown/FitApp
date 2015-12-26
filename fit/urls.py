from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'^index', views.index, name='home'),
		url(r'^about', views.about, name='about'),
		url(r'^game', views.game, name='game'),
]