from django.conf.urls import url
from django.views.generic import TemplateView

from presentation import views

urlpatterns = [
    url(
        r'^$',
        TemplateView.as_view(template_name='presentation/home.html'),
        name='home'
    ),
    url(r'^presentation/description$', views.description, name='description'),
    url(
        r'^presentation/acces$',
        TemplateView.as_view(template_name='presentation/entrance.html'),
        name='entrance'
    ),
    url(
        r'^webmaster$',
        TemplateView.as_view(template_name='presentation/webmaster.html'),
        name='webmaster'
    ),
]
