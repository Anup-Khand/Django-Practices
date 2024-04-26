from django.urls import path
from . import views
urlpatterns = [
    path("thirdapp/", views.thirdapp),
]
