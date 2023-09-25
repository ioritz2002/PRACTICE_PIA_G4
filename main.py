#!/usr/bin/env python3

import objetos_y_clases
import json
import plantilla_metodos

from datetime import datetime

file_name = "personas.json"




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
    #persona = objetos_y_clases.Persona()
    #persona.nombre = input("Introduce el nombre\n")
    #persona.apellidos = input("Introduce los apellidos\n")
    #Fecha en formato string
    #fecha = input("Introduce la fecha de nacimiento en formato dd/mm/aaaa\n")
    #persona.fecha_nacimiento = set_fecha_nacimiento(fecha)

    #plantilla_metodos.write(persona, file_name)
    
    personas = []
    personas = plantilla_metodos.read_objects(file_name)

    for p in personas:
        if p.nombre == "xabi":
            key = p.nombre
            p.nombre = "xabier"
            plantilla_metodos.update(p, key, file_name)
    #Lee el json y lo guarda en una lista de objetos de tipo Persona para poder utilizarlo
   # with open("personas.json", "r") as archivo:
    #    contenido = archivo.read()
        
     #   if contenido:
     #       datos = json.loads(contenido)

      #      for d in datos:
       #         persona = objetos_y_clases.Persona()
        #        persona.nombre = d["nombre"]
         #       persona.apellidos = d["apellidos"]
          #      persona.fecha_nacimiento = d["fecha_nacimiento"]

           #     personas.append(persona)
    
   # persona = personas[0]
    #print(persona.nombre)

    #Esto lee el archivo y lo guarda como un objeto json
    #with open("personas.json", "r") as archivo:
    #    datos = json.load(archivo)

    #Recorre el diccionario entero y modifica el que quiere
    #for persona in datos:
     #   if persona["nombre"] == "jaime":
      #      persona["apellidos"] = "rodriguez"

    #Actualiza el elemento modificado en el json
    #with open("personas.json", "w") as archivo:
     #   json.dump(datos, archivo, indent=4)

run()
