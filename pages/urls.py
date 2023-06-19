from django.urls import path

from .views import HomePageView, NoPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="Home"),
    path("No/", NoPageView.as_view(), name="No"),
]