from django.contrib import admin
from .models import Comunidad,Evento,Solicitud,AgentesPatorales,Login
# Register your models here.
admin.site.register(Comunidad)
admin.site.register(Evento)
admin.site.register(Solicitud)
admin.site.register(Login)
admin.site.register(AgentesPatorales)