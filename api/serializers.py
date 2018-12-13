from rest_framework import serializers
from core.models import Comunidad,Evento,Solicitud,AgentesPatorales




class ComunidadSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comunidad
        fields=('id','nombre','ubicacion','nombreCordinadores','nombresAgentesPastorales','nombresMisnistroComunion')


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Evento
        fields=('id','nombre','tipo','fecha','hora','comunidad')

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model= Solicitud
        fields=('id','sacramento','nombreP','apellidoP','nombreH','apellidoH')

class AgenteSerializer(serializers.ModelSerializer):
    class Meta:
        model= AgentesPatorales
        fields=('id','nombre','apellido','edad','comu')