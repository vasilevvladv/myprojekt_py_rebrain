from rest_framework import generics

from .models import Server
from .serializer import ServerSerializer, ServerStatusSerializer


class ServerViewSet(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerAddView(generics.CreateAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerStatusSet(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerStatusSerializer
