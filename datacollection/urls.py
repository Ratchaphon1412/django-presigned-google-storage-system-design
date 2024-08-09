from django.urls import path
from .views import UploadView
urlpatterns = [
    path("upload/",UploadView.as_view()),
    path("file/<str:key>/",UploadView.as_view())
]