from django.urls import path
from .views import gethomepage

urlpatterns = [
    path('', gethomepage, name="home")
]