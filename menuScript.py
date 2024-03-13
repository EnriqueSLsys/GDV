import json_PRUEBAS
import Gest_BD_Json
import getpass

def menu():
    print("\nMenú:")
    print("1. Información de vehículos")
    print("2. Gestión de base de datos")
    print("3. Salir")

def gestion_base_de_datos():
    servidor = input("Ingrese la dirección del servidor MySQL (por defecto localhost): ") or "localhost"
    usuario = input("Ingrese el nombre de usuario de MySQL: ")
    password = getpass.getpass("Ingrese la contraseña de MySQL: ")
    nombre_bd = input("Ingrese el nombre de la base de datos MySQL: ")
    # Llama a la función main del módulo Gest_BD_Json que guarda los argumentos - parametros
    Gest_BD_Json.main(servidor, usuario, password, nombre_bd)  

def main():
    opcion = None
    while opcion != "3":
        menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            json_PRUEBAS.main()
        elif opcion == "2":
            gestion_base_de_datos()
        elif opcion == "3":
            print("\n¡Adiós!")
        else:
            print("\nOpción no válida")

if __name__ == "__main__":
    main()
