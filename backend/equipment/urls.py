from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.upload_csv, name='upload_csv'),
    path('summary/latest', views.get_latest_summary, name='latest_summary'),
    path('history', views.get_history, name='history'),
    path('history/<int:pk>', views.get_dataset_detail, name='dataset_detail'),
]
