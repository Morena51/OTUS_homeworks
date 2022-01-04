from django.urls import path
from . import views


urlpatterns = [
    path('', views.api),
    path('e2e', views.e2e),
    path('api', views.api),
    path('unit', views.unit)
]
