from django.contrib import admin
from django.urls import path
from home import views

#added manually
urlpatterns = [
   path("", views.index, name='home'),
   path("about", views.about, name='about'),
   path("services", views.services, name='services'),
   path("contact", views.contact, name='contact'),
   path("pcb",    views.pcb,      name="pcb"),
   path('login',views.loginUser, name='login'),
   path('logout',views.logoutUser, name='logout'),
   
]  