
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index_page"),
    path('home/', views.simple_view, name="home"),
    path('aboutuss/', views.call, name="about us"),
    path('new/', views.new, name="new"),
    path('form/', views.form, name="form")
]
