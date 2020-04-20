from django.urls import path
from . import views
from permits.views import PermitProfileListView

urlpatterns = [
    path('', views.home, name='home'),
    path('truck/', views.truck, name='truck'),
    path('sub/', views.sub, name='sub'),
    path('contact/', views.contact, name='contact'),
    path('agency/', views.agency, name='agency'),
    path('insurance/', views.insurance, name='insurance'),
    path('permit/', PermitProfileListView.as_view(), name='permit'),
]
