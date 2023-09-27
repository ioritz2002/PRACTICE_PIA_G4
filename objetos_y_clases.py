#!/usr/bin/env python3
#Esto de aqui es de ioritz
import datetime
import json
class Persona:
 
    def __init__(self, dni=None, nombre=None, apellidos=None, fecha=None):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha
