#!/usr/bin/env python3

import objetos_y_clases
import json
import plantilla_metodos

from datetime import datetime

file_name = "personas.json"

out=False

while out!=True:
    command=input("Introduce una opcion:\n"
                  "1º Crear\n"
                  "2º Leer\n"
                  "3º Actualizar\n"
                  "4º Borrar\n"
                  "5º Salir del programa\n")
    match command:
        case "1":
            print("Opcion seleccionada 1:\n")

            def set_fecha_nacimiento(fecha):
                try:
                    #Esto lo formatea a un datetime
                    fecha_nacimiento = datetime.strptime(str(fecha), "%d/%m/%Y")
                    #Esto lo formatea a string pero en un formato que se quiera
                    return fecha_nacimiento.strftime("%d/%m/%Y")
                except Exception:
                    print("Fecha incorrecta")

                #Creamos el objeto y le introducimos los datos
            persona = objetos_y_clases.Persona()
            persona.nombre = input("Introduce el nombre\n")
            persona.apellidos = input("Introduce los apellidos\n")
                #Fecha en formato string
            fecha = input("Introduce la fecha de nacimiento en formato dd/mm/aaaa\n")
            persona.fecha_nacimiento = set_fecha_nacimiento(fecha)

            plantilla_metodos.write(persona, file_name)
            personas = plantilla_metodos.read(file_name)
            print(personas)
        case "2":
            print("Opcion seleccionada 2:\n")
            personas = plantilla_metodos.read(file_name)
            print(personas)
        case "3":
            print("Opcion seleccionada 3:\n")
            plantilla_metodos.write(persona, file_name)
            personas = plantilla_metodos.read(file_name)
            print(personas)

            personas = []
            personas = plantilla_metodos.read_objects(file_name)
            print(personas)
            print(personas[0].nombre)

            for p in personas:
                if p.nombre == "xabi":
                    key_value = p.nombre
                    p.nombre = "xabier"
                    plantilla_metodos.update(p, key_value, file_name)
        case "4":
            print("Opcion seleccionada 4:\n")
        case "5":
            out=True
            print("Has salido del programa correctamente")
        case other:
            print("Error")
  


