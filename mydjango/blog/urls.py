from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^page/(?P<article_id>[0-9]+)', views.article_page, name='article_page'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^action/', views.edit_action, name='edit_action'),
]
