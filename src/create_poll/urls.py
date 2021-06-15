from django.urls import path
from . import views

urlpatterns = [
    path('', views.createPoll, name="create_poll")
]
