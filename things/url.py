from django.urls import path
from things import views
urlpatterns = [
    path('', views.home, name='home'),

    
]
