from gestionusuarios.models import usuariooperador,registro
from django.shortcuts import render
from django.http import HttpResponse, request
from django.db import models


# Create your views here.

def datos_vuelo(request):
    if request.GET["usuario"]:
        if request.GET["contraseña"]:
            nombre=request.GET["usuario"]
            A=usuariooperador.objects.filter(usuario__icontains=nombre)
            if A:
                contra=request.GET["contraseña"]
                B=usuariooperador.objects.filter(contraseña__icontains=contra)
                if B:
                    return render(request, "boleto.html")
                else:
                    B="Contraseña Incorrecta"
                    return HttpResponse(B)    
            else:
                B="usuario no encontrado"
                return HttpResponse(B)
            #if user==nombre:
             #   return render(request, "boleto.html")
            #else:
             #   mensaje="Error el usuario no existe"
              #  return HttpResponse(mensaje)
        else:
            mensaje="Error Ingrese contraseña"
            return HttpResponse(mensaje)
    else:
        mensaje="Error Ingrese nombre"
        return HttpResponse(mensaje)


def mostrar_datos(request):
    datos=registro.objects.all()
    return render(request,"resultados_busqueda.html",{"datos":datos})

def borrar(request):
    datos=registro.objects.all()
    datos.delete()
    mensaje="Datos Borrados"
    return HttpResponse(mensaje)

def sesion(request):

    return render(request, "sesion.html")

def guardar(request):
    if request.GET["clase"]:
        if request.GET["comida"] or request.GET["bebida"] or request.GET["pelicula"]:
            c1=request.GET["clase"]
            clas=int(c1)
            a1=request.GET["comida"]
            alimento=int(a1)
            b1=request.GET["bebida"]
            bebid=int(b1)
            p=request.GET["pelicula"]
            peli=int(p)

            if clas==1:
                pcomi=50
                pbeb=35
                ppeli=70
                clase=1

            elif clas==2:
                pcomi=40
                pbeb=25
                ppeli=55
                clase=2
        
            elif clas==3:
                pcomi=25
                pbeb=10
                ppeli=25
                clase=3

            sercombeb= alimento + bebid
            sertotal= sercombeb+peli
            servicio=str(sertotal)
            serpri=(alimento> 0) & (bebid>0)
            serprima=serpri & (peli>0)
            serprimera=serprima & (clas==1)
            serquince=serprimera & (sertotal >=10)

            subcombeb= alimento*pcomi + bebid*pbeb
            subtot= subcombeb+peli*ppeli
            subtotal2=(str(subtot))


            if serquince==1:
                desc=subtot*0.15
                descuento2=(str(desc))  

            elif serprimera==1:
                desc=subtot*0.05
                descuento2=(str(desc))
              
            elif sertotal >=10:
                desc=subtot*0.1
                descuento2=(str(desc))

            else :
                desc=0
                descuento2=(str(desc))

            tot=subtot - desc
            total2=(str(tot))

            p1=registro(clase=clas, subtotal=subtotal2, total=total2, descuento=descuento2)
            p1.save()
            mensaje="Datos guardatos"
            return HttpResponse(mensaje)
        else:
            mensaje="Advertencia, debe ingresar algun servicio"
            return HttpResponse(mensaje)
    else:
        mensaje="No ingresó la clase del vuelo"
        return HttpResponse(mensaje)