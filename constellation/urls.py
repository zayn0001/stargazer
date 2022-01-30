from django.urls import include, path
from . import views
import constellation

app_name = "constellation"
urlpatterns = [
    path("", views.index, name="index"),
    path("possibilities", views.possibilities, name="possibilities"),
    path('solution', views.solution, name='solution')
]