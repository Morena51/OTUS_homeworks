from django.urls import path
from . import views
from .api_coverage.views import ApiCoverageView

urlpatterns = [
    path('', views.api),
    path('allure', views.allure),
    path('api', views.api),
    path('api/coverage', ApiCoverageView.as_view()),
]
