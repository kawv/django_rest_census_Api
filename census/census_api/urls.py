from django.urls import path

from census_api import views

urlpatterns = [
    path('citizen',views.CitizenViewSet)
,
]
