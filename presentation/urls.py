from django.conf.urls import url

from presentation import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^description$', views.description, name='description'),
]
