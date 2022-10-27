from django.urls import path

from . import views

app_name = 'mylibrary'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('inquiry/', views.InquiryForm.as_view(), name='inquiry'),
]