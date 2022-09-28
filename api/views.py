from rest_framework import generics
from .serializers import ProgramSerializer
from programs.models import Program
# Create your views here.


class ProgramListAPIView(generics.ListAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()


class ProgramRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
