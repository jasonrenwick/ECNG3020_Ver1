from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^gitpage/', views.gitpage, name='gitpage')
]
