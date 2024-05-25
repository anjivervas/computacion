import json #importa la biblioteca json
from dos import nombre, apellido, periodo, promedio, agregar_estudiante, eliminar_estudiante #importa las funciones que se encuentran en el archivo dos.py

def menu(): #definición del menú
    print("\n".join([ #imprimir el menú
        "",
        "Menú:",
        "1. Nombre",
        "2. Apellido",
        "3. Periodo",
        "4. Promedio",
        "5. Agregar Estudiante",
        "6. Eliminar Estudiante",
        "7. Salir"
    ]))

while True: #bucle para repetición del menú
    menu() #muestra el menú
    opcion = input("Seleccione una opción: ") #le dice al usuario que elija una opción

    if opcion == "1": #evaluación de la opción
        cedula = input("Ingrese el número de cédula: ")
        print(nombre(cedula))
    elif opcion == "2":
        cedula = input("Ingrese el número de cédula: ") #llama la función
        print(apellido(cedula))
    elif opcion == "3":
        cedula = input("Ingrese el número de cédula: ")
        print(periodo(cedula))
    elif opcion == "4":
        promedio()
    elif opcion == "5":
        agregar_estudiante()
    elif opcion == "6":
        eliminar_estudiante()
    elif opcion == "7":
        break #termina el bucle
    else:
        print("Opción inválida")
        break