from django.urls import path, include
from healthz_view import healthz

urlpatterns = [
    path('api/healthz', healthz, name='healthz'),
    path('api/', include('api.urls')),
]
