def main():

    nombre = input("Por favor, ingresa tu nombre: ")
    edad = input("Ahora, ingresa tu edad: ")

    print("Tu nombre es:", nombre)
    print("Tu edad es:", edad)

if __name__ == "__main__":
    main()
#2
import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area


radio_del_circulo = 5.0
area_del_circulo = calcular_area_circulo(radio_del_circulo)
print("El área del círculo con radio", radio_del_circulo, "es:", area_del_circulo)

#3
import random

def generar_lista_aleatoria(longitud_lista, rango_inferior, rango_superior):
    lista_aleatoria = [random.randint(rango_inferior, rango_superior) for _ in range(longitud_lista)]
    return lista_aleatoria

def main():

    longitud_lista = int(input("Ingrese la longitud de la lista aleatoria: "))
    rango_inferior = int(input("Ingrese el rango inferior de los números aleatorios: "))
    rango_superior = int(input("Ingrese el rango superior de los números aleatorios: "))


    lista_aleatoria = generar_lista_aleatoria(longitud_lista, rango_inferior, rango_superior)


    print("Lista aleatoria generada:", lista_aleatoria)

if __name__ == "__main__":
    main()
