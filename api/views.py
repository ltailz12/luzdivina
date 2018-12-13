from django.shortcuts import render
from rest_framework import generics
from core.models import Comunidad, Evento,AgentesPatorales,Solicitud
from .serializers import ComunidadSerializer, EventoSerializer,AgenteSerializer,SolicitudSerializer

# Create your views here.

class ComunidadLista(generics.ListCreateAPIView):
    queryset=Comunidad.objects.all()
    serializer_class=ComunidadSerializer

class ComunidadDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset= Comunidad.objects.all()
    serializer_class=ComunidadSerializer

class EventoLista(generics.ListCreateAPIView):
    queryset=Evento.objects.all()
    serializer_class=EventoSerializer    



class EventoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset= Evento.objects.all()
    serializer_class=EventoSerializer

class SolicitudLista(generics.ListCreateAPIView):
    queryset=Solicitud.objects.all()
    serializer_class=SolicitudSerializer    



class SolicitudDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset= Solicitud.objects.all()
    serializer_class=SolicitudSerializer

class AgenteLista(generics.ListCreateAPIView):
    queryset=AgentesPatorales.objects.all()
    serializer_class=AgenteSerializer    



class AgenteDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset= AgentesPatorales.objects.all()
    serializer_class=AgenteSerializer




