from django.conf.urls import url
from .views import ComunidadDetalle,ComunidadLista,EventoLista,EventoDetalle,SolicitudDetalle,SolicitudLista,AgenteLista,AgenteDetalle


urlpatterns = [
    url('comunidad_lista/',ComunidadLista.as_view()),
    url(r'^comunidad_detalle/(?P<pk>[0-9]+)/$',ComunidadDetalle.as_view()),
    url('evento_lista/',EventoLista.as_view()),
    url(r'^evento_detalle/(?P<pk>[0-9]+)/$',EventoDetalle.as_view()),
     url('solicitud_lista/',SolicitudLista.as_view()),
    url(r'^solictud_detalle/(?P<pk>[0-9]+)/$',SolicitudDetalle.as_view()),
     url('agente_lista/',AgenteLista.as_view()),
    url(r'^agente_detalle/(?P<pk>[0-9]+)/$',AgenteDetalle.as_view()),
]