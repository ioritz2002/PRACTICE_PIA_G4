#!/usr/bin/env python3

import objetos_y_clases
import json

from datetime import datetime


def set_fecha_nacimiento(fecha):
    try:
        fecha_nacimiento = datetime.strptime(str(fecha), "%d/%m/%Y")
        return fecha_nacimiento.strftime("%d/%m/%Y")
    except Exception:
        print("Fecha incorrecta")

    


def run():
    persona = objetos_y_clases.Persona()
    persona.nombre = input("Introduce el nombre\n")
    persona.apellidos = input("Introduce los apellidos\n")
    fecha = input("Introduce la fecha de nacimiento en formato dd/mm/aaaa\n")
    persona.fecha_nacimiento = set_fecha_nacimiento(fecha)

    personas = []
    with open("personas.json", "r") as archivo:
        contenido = archivo.read()
        personas = json.loads(contenido) if contenido else []
   
        

    personas.append(persona.__dict__)

    with open("personas.json", "w") as archivo:
        archivo.write(json.dumps(personas, indent=4))


    with open("personas.json", "r") as archivo:
        contenido = archivo.read()
        personas = json.loads(contenido) if contenido else []
    


    for i in personas:
        print(i)
    

run()
