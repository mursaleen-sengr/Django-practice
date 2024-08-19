
from django.urls import path, include
from . import views


#localhost:8000/core/
urlpatterns = [
    
    path('', views.core, name='core'),
    
    
]