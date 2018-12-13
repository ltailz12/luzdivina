from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'), 
    path('lpE/',views.ListadoEvento,name='ListadoEvento'),
    path('lpC/',views.ListadoComunidad,name='ListadoComunidad'),   
    path('lpS/',views.ListadoSolicitud,name='ListadoSolicitud'), 
    path('lpA/',views.ListadoAgente,name='ListadoAgente'),  
    path ('formu/',views.Formulario,name='formulario'),
    path ('formuE/',views.FormularioEvento,name='formularioEvento'),
    path ('formuS/',views.FormularioSolicitud,name='formularioSolicitud'),
    path ('formuA/',views.FormularioAgente,name='formularioAgente'),
    path ('login/',views.FormularioLogin,name='login'),
    path ('home/',views.Home1,name='hola'),
    
    
]