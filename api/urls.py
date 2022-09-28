from django.urls import path
from .views import ProgramListAPIView, ProgramRetrieveAPIView
urlpatterns = [
    path('', ProgramListAPIView.as_view()),
    path('<int:pk>', ProgramRetrieveAPIView.as_view())
]
