#!/usr/bin/env python3

# Clase llamada "Vehiculos"
class Vehiculos:
    
    # Constructor de la clase (inicializa los atributos)
    def __init__(self, marca, cv, edad):
        self.marca = marca
        self.cv = cv
        self.edad = edad

    # Método para imprimir información sobre el vehiculo
    def presentarse(self):
        print(f"Hola, el vehiculo es {self.marca} , tiene {self.cv} caballos de potencia y el vehiculo tiene {self.cv} años.")

# Creación de objetos (instancias) de la clase Vehiculo
Vehiculo1 = Vehiculos("Ferrari", 700, 2)
Vehiculo2 = Vehiculos("Mercedes", 530, 4)
Vehiculo3 = Vehiculos("Lamborghini", 650, 1)
Vehiculo4 = Vehiculos("Bugatti", 830, 3)

# Acceso a los atributos y llamada a métodos de los objetos
print(Vehiculo1.marca)  # Imprime "Ferrari"
print(Vehiculo2.edad)  # Imprime 4
print(Vehiculo4.cv)  # Imprime 830


Vehiculo1.presentarse()  # Imprime "Hola, el vehiculo es Ferrari , tiene 700 caballos de potencia y el vehiculo tiene 2 años."
Vehiculo4.presentarse()  # Imprime "Hola, el vehiculo es Bugatti , tiene 830 caballos de potencia y el vehiculo tiene 3 años."
