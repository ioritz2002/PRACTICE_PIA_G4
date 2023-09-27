import json
import objetos_y_clases

def write(obj, file_name):
    objs = []
    objs = read(file_name)
    objs.append(obj.__dict__)
    
    with open(file_name, "w") as archivo:
        archivo.write(json.dumps(objs, indent=4))
    pass

#Lee en formato string
def read(file_name):
    objs = []

    try:

        with open(file_name, "r") as archivo:
            contenido = archivo.read()
            objs = json.loads(contenido) if contenido else []
        
        return objs
    except FileNotFoundError:
        with open(file_name, "w") as archivo:
            archivo.write(json.dumps(objs, indent=4))

        return []

#Adaptarlo a las necesidades del software
#Retorna una lista de objetos de lo que se guarda en python
def read_objects(file_name):
    objs = []

    try:

        with open(file_name, "r") as archivo:
            contenido = archivo.read()
            
            if contenido:
                datos = json.loads(contenido)

                for d in datos:
                    persona = objetos_y_clases.Persona()
                    persona.dni = d["dni"]
                    persona.nombre = d["nombre"]
                    persona.apellidos = d["apellidos"]
                    persona.fecha_nacimiento = d["fecha_nacimiento"]

                    objs.append(persona)
        
        return objs
    except FileNotFoundError:
        with open(file_name, "w") as archivo:
            archivo.write(json.dumps(objs, indent=4))

        return []
#Modificar en funcion de las necesidades del software
def delete(dni, file_name):
    

    try:
        objs = read(file_name)
        new_list = []

        for i in objs:
            if i["dni"] != dni:
                new_list.append(i)

        with open(file_name, "w") as archivo:
            json.dump(new_list, archivo, indent=4)

        
        
    except FileNotFoundError:
        raise Exception("El fichero no existe")

    pass

    

    
#Actualiza 
#Adaptarlo a las necesidades del sofware
def update(obj, key_value, file_name):
    with open(file_name, "r") as archivo:
        datos = json.load(archivo)
    
    for persona in datos:
        if persona["nombre"] == key_value:
            persona["nombre"] = obj.nombre

    with open(file_name, "w") as archivo:
        json.dump(datos, archivo, indent=4)

    pass

