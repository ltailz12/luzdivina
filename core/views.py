from django.shortcuts import render
from .models import Comunidad,Evento,Solicitud,AgentesPatorales,Login

# Create your views here.
def Home(request):
    return render(request,'core/index.html')

def ListadoComunidad(request):
    listaComunidad = Comunidad.objects.all()
    return render(request,'core/listarComunidad.html',{'listaComunidad':listaComunidad})

def ListadoEvento(request):
    listaEvento = Evento.objects.all()
    return render(request,'core/listarEvento.html',{'listaEvento':listaEvento})

def ListadoSolicitud(request):
    listaSolicitud = Solicitud.objects.all()
    return render(request,'core/listarSolicitud.html',{'listaSolicitud':listaSolicitud})

def ListadoAgente(request):
    listaAgente = AgentesPatorales.objects.all()
    return render(request,'core/listarAgente.html',{'listaAgente':listaAgente})



def Formulario(request):
    lt= Comunidad.objects.all()#select * from Tipos
    if request.POST:
        nombre= request.POST["nombre"]
        ubicacion=request.POST["ubicacion"]
        nombreCordinadores=request.POST["nombreCordinadores"]
        nombresAgentesPastorales=request.POST["nombresAgentesPastorales"]
        nombresMisnistroComunion=request.POST["nombresMisnistroComunion"]
       

     

        comun= Comunidad(
            nombre=nombre,
            ubicacion=ubicacion,
            nombreCordinadores=nombreCordinadores,
            nombresAgentesPastorales=nombresAgentesPastorales,
            nombresMisnistroComunion=nombresMisnistroComunion
           
        )
        comun.save()
        return render(request,'core/formulario_ingreso.html',
                              {'tipos':lt,'mensaje':'grabo'})

    return render(request,'core/formulario_ingreso.html',{'tipos':lt})

def FormularioSolicitud(request):
    po= Solicitud.objects.all()#select * from Tipos
    if request.POST:
        sacramento= request.POST["sacramento"]
        nombreP=request.POST["nombreP"]
        apellidoP=request.POST["apellidoP"]
        nombreH=request.POST["nombreH"]
        apellidoH=request.POST["apellidoH"]
       

     

        soli= Solicitud(
            sacramento=sacramento,
            nombreP=nombreP,
            apellidoP=apellidoP,
            nombreH=nombreH,
            apellidoH=apellidoH
           
        )
        soli.save()
        return render(request,'core/formulario_solicitud.html',
                              {'tipos':po,'mensaje':'grabo'})

    return render(request,'core/formulario_solicitud.html',{'tipos':po})      

def FormularioEvento(request):
    lp= Comunidad.objects.all()#select * from Tipos
    if request.POST:
        nombre= request.POST["nombre"]
        tipo=request.POST["tipo"]
        fecha=request.POST["fecha"]
        hora=request.POST["hora"]
        comunidad=request.POST["comunidad"]
       
        obj_tipo= Comunidad.objects.get(id=comunidad)
     

        evento= Evento(
            nombre=nombre,
            tipo=tipo,
            fecha=fecha,
            hora=hora,
            comunidad=obj_tipo
           
        )
        evento.save()
        return render(request,'core/formulario_ingresoE.html',
                              {'tipos':lp,'mensaje':'grabo'})

    return render(request,'core/formulario_ingresoE.html',{'tipos':lp})

def FormularioAgente(request):
    ko= Comunidad.objects.all()#select * from Tipos
    if request.POST:
        nombre= request.POST["nombre"]
        apellido=request.POST["apellido"]
        edad=request.POST["edad"]
        tipoPersona=request.POST["tipoPersona"]
        comu=request.POST["comu"]
       
        obj_tipo= Comunidad.objects.get(id=comu)
     

        agente= AgentesPatorales(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            tipoPersona=tipoPersona,
            comu=obj_tipo
           
        )
        agente.save()
        return render(request,'core/formulario_Agente.html',
                              {'tipos':ko,'mensaje':'grabo'})

    return render(request,'core/formulario_Agente.html',{'tipos':ko})        

def FormularioLogin(request):
   #select * from Tipos
    if request.POST:
        usuario= request.POST["usuario"]
        password=request.POST["password"]        
        try:
            me=Login.objects.get(usuario=usuario,password=password)
            if me.usuario is not None:
                request.session["usuario"]=usuario
                return render(request,'core/home.html',{'mensaje':'encontro'})            
        except Exception as identifier:
            return render(request,'core/login.html',{'mensaje':'no ta'})                            

    return render(request,'core/login.html',{'mensaje':'ingrese'})

def Home1(request):
     return render(request,'core/home.html')

