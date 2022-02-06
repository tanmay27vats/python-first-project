from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('contact/', contact_views.contact_view, name='contact'),
]