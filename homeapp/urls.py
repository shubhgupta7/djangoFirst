from django.contrib import admin
from django.urls import path,include
from homeapp import views

urlpatterns = [
    path("home",views.home,name="homepage_welcome"),
    path("about", views.about, name="homepage_welcome"),
    path("contact", views.contact, name="homepage_welcome"),
    path("service", views.service, name="homepage_welcome"),
    path("projects", views.projects, name="homepage_welcome"),

]
