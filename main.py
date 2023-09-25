#!/usr/bin/env python3

import objetos_y_clases
import json

from datetime import datetime

#Metodo para setear fecha de nacimento en formato valido para json
def set_fecha_nacimiento(fecha):
    try:
        #Esto lo formatea a un datetime
        fecha_nacimiento = datetime.strptime(str(fecha), "%d/%m/%Y")
        #Esto lo formatea a string pero en un formato que se quiera
        return fecha_nacimiento.strftime("%d/%m/%Y")
    except Exception:
        print("Fecha incorrecta")

    


def run():
    #Creamos el objeto y le introducimos los datos
    persona = objetos_y_clases.Persona()
    persona.nombre = input("Introduce el nombre\n")
    persona.apellidos = input("Introduce los apellidos\n")
    #Fecha en formato string
    fecha = input("Introduce la fecha de nacimiento en formato dd/mm/aaaa\n")
    persona.fecha_nacimiento = set_fecha_nacimiento(fecha)
    
    #Una lista vacia de personas
    personas = []

    #Abrimos el archivo en modo lectura para ver si el archivo esta vacio
    #o por el contrario hay datos ya introducidos, en caso de que haya datos introducidos
    #los lee y los guarda en la lista de personas
    with open("personas.json", "r") as archivo:
        contenido = archivo.read()
        personas = json.loads(contenido) if contenido else []
   
    #Añadimos a la lista de personas el objeto de persona creado por nosotros y lo guardamos como diccionario
    personas.append(persona.__dict__)

    #Esto escribe en el json
    with open("personas.json", "w") as archivo:
       archivo.write(json.dumps(personas, indent=4))

    #Esto lee el json y lo guarda como strings y por tanto no se puede usar como objeto del tipo persona
    with open("personas.json", "r") as archivo:
        contenido = archivo.read()
        personas = json.loads(contenido) if contenido else []
    
    personas = []

    #Lee el json y lo guarda en una lista de objetos de tipo Persona para poder utilizarlo
    with open("personas.json", "r") as archivo:
        contenido = archivo.read()
        
        if contenido:
            datos = json.loads(contenido)

            for d in datos:
                persona = objetos_y_clases.Persona()
                persona.nombre = d["nombre"]
                persona.apellidos = d["apellidos"]
                persona.fecha_nacimiento = d["fecha_nacimiento"]

                personas.append(persona)
    
    persona = personas[0]
    print(persona.nombre)
run()
