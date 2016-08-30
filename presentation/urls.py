from django.conf.urls import url

from presentation import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
