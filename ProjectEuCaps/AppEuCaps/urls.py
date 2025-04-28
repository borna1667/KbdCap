from django.urls import path
from . import views  # <-- here you import your own views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('landing_page/', views.landing_page, name='landing_page_direct'),
]
