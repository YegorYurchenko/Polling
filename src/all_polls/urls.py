""" All_polls URL configuration """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_polls, name="all_polls"),
    path('<int:pk>', views.PollDetailView.as_view(), name="selected_poll"),
    path('result_<int:pk>', views.GetResult.as_view(), name="poll_result"),
]
