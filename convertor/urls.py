from django.urls import path

from .views import ConvertorView


urlpatterns = [
    path('convert/', ConvertorView.as_view()),
]
