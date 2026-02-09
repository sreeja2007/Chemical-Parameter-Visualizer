from django.urls import path
from . import views

urlpatterns = [
    path('pdf', views.generate_pdf_report, name='pdf_report'),
]
