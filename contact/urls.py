from django.conf.urls import url
from django.views.generic import TemplateView

from contact import views

urlpatterns = [
    url(r'^$', views.contact, name='contact'),
]
