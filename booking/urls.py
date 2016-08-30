from django.conf.urls import url

from booking import views

urlpatterns = [
    url(r'^$', views.home, name='booking-home'),
    url(r'^reserver/$', views.booking, name='booking'),
    url(r'^calendrier/$', views.calendar, name='calendar'),
]
