
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', renderIndex, name = "render_home"),
]
