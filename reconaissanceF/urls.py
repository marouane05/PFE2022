
from django.urls import path, include
from .views import (
    PersonListApiView,
)


urlpatterns = [
    path('api', PersonListApiView.as_view()),
    ]