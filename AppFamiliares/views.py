from contextvars import Context
from multiprocessing import context
from pipes import Template
from re import TEMPLATE
from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import context, Template
from django.template import loader



# Create your views here.

def familia(self):
    familia=Familiares(nombre="Catalina",edad=1,fecha_nacimiento="2020-11-06",parentesco="Hija")
    familia.save()

    familia2=Familiares(nombre="Emilia",edad=82,fecha_nacimiento="1939-12-22",parentesco="Madre")
    familia2.save()
 
    familia3=Familiares(nombre="Enrique",edad=85,fecha_nacimiento="1937-06-29",parentesco="Padre")
    familia3.save()

    fam1=f"Nombre: {familia.nombre}, Edad: {familia.edad}, Fecha_nacimiento: {familia.fecha_nacimiento}, Parentesco: {familia.parentesco}"
    fam2=f"Nombre: {familia2.nombre}, Edad: {familia2.edad}, Fecha_nacimiento: {familia2.fecha_nacimiento}, Parentesco: {familia2.parentesco}"
    fam3=f"Nombre:{familia3.nombre}, Edad: {familia3.edad}, Fecha_nacimiento: {familia3.fecha_nacimiento}, Parentesco: {familia3.parentesco}"
    diccionario= {'familia1':fam1, 'familia2':fam2, 'familia3':fam3}
   
    
    plantilla=loader.get_template('TemplateFamiliares.html')
    familiares=plantilla.render(diccionario)
    return HttpResponse (familiares)


    



    
    