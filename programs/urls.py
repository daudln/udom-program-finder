from django.urls import path
from .views import *


urlpatterns = [
    path('programs/', ProgramListView.as_view(), name='program_list'),
    path('programs/<int:pk>', ProgramDetailView.as_view(), name='program_detail'),
]
