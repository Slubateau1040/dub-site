from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_riddim, name='list_riddim'),
    path('<int:riddim_id>/', views.detail_riddim, name='detail_riddim'),
]