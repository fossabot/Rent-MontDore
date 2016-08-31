from django.conf.urls import url
from django.views.generic import TemplateView

from booking import views

urlpatterns = [
    url(
        r'^tarifs/$',
        TemplateView.as_view(template_name='booking/price.html'),
        name='booking-home-price'
    ),
    url(r'^reservation/$', views.booking, name='booking'),
    url(r'^calendrier/$', views.calendar, name='calendar'),
]
