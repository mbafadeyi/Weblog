from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("<slug:post>/", views.post_detail, name="post_detail"),
]
