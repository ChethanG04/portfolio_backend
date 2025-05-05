from django.urls import path
from . import views

urlpatterns = [
    path('', views.save_portfolio, name='save_portfolio'),  # <-- this line for home
    path('submit/', views.save_portfolio, name='save_portfolio'),  # keep this also
]
