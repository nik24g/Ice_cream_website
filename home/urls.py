from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Nitin Ice Cream Admin"
admin.site.site_title = "Nitin Ice Cream Admin Portal"
admin.site.index_title = "Welcome to Nitin Ice Creams"

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path('signin', views.signin, name="signin"),
    path('logout', views.logoutuser, name="logout"),
    path('signup', views.signup, name="signup"),
]