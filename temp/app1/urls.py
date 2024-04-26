from django.urls import path
from app1 import views


urlpatterns = [
    path('Simple/', views.Simple_view, name="view1")
]
