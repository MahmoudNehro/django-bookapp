from django.urls import path
from .views import getoneauthor

urlpatterns = [
    path('<int:author_id>', getoneauthor, name="author_page")
]