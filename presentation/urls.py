from django.conf.urls import url
from django.views.generic import TemplateView

from presentation import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='presentation/home.html'), name='home'),
    url(r'^description$', TemplateView.as_view(template_name='presentation/description.html'), name='description'),
    url(r'^acces$', TemplateView.as_view(template_name='presentation/entrance.html'), name='entrance'),
]
