from django.urls import path

from . import views

app_name = 'mylibrary'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('inquiry/', views.InquiryForm.as_view(), name='inquiry'),
    path('document-list/', views.DocumentListView.as_view(), name='document_list'),
    path('document-detail/<int:pk>/', views.DocumentDetailView.as_view(), name='document_detail'),
    path('document-create/', views.DocumentCreateView.as_view(), name='document_create'),
    path('document-update/<int:pk>/', views.DocumentUpdateView.as_view(), name='document_update'),
    path('document-delete/<int:pk>/', views.DocumentDeleteView.as_view(), name='document_delete'),
]