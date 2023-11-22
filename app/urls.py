from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('clear/', views.ClearDataView.as_view(), name='clear_data'),
    path('refresh/', views.RefreshDataView.as_view(), name='refresh_data'), 
]
