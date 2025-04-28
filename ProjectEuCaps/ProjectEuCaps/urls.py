from django.contrib import admin
from django.urls import path, include  # <-- important

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppEuCaps.urls')),  # <-- connect to app urls
]
