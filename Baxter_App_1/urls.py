from django.urls import path
from Baxter_App_1.views import home

urlpatterns = [
    path('home/', home, name="home"),
]
