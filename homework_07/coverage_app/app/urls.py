from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    path('', views.ProjectListView.as_view()),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(),
         name='project_detail'),
    path('e2e', views.e2e),
    path('api', views.api),
    path('unit', views.unit),
    path('e2e/list', views.E2EListView.as_view(),
         name='e2e_list'),
    path('e2e/<int:pk>/', views.E2EDetailView.as_view(),
         name='e2e_detail'),
    path('api/list', views.APIListView.as_view(),
         name='api_list'),
    path('unit/list', views.UNITListView.as_view(),
         name='unit_list'),
]
