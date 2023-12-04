from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('segment_settings', views.segment_settings, name='segment_settings'),
    path('profile_settings', views.profile_settings, name='profile_settings'),
    path('aws_s3', views.aws_s3, name='aws_s3'),
    path('rest_api', views.rest_api, name='rest_api'),

    path('api_fetch_code', api.fetch_code_component, name='api_fetch_code'),

    path('codecomponents', views.CodeComponentListView.as_view(), name='codecomponents'),
    path('codecomponent_create', views.CodeComponentCreateView.as_view(), name='codecomponent_create'),
    path('codecomponent_edit/<int:pk>/', views.CodeComponentEditView.as_view(), name='codecomponent_edit'),

    path('login', views.loginUser, name ='login'),
    path('register', views.registerUser, name ='register'),
    path('logout', views.logoutUser, name ='logout'),
]