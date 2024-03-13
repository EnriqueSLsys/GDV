import json

def mostrar_informacion_pizza(pizza):
    print("\nInformación de la pizza:")
    print(f"Tamaño: {pizza['tamaño']}")
    print(f"Precio: ${pizza['precio']}")
    print("Toppings:")
    for topping in pizza['toppings']:
        print(f" - {topping}")
    print("Cliente:")
    cliente = pizza['cliente']
    print(f"Nombre: {cliente['nombre']}")
    print(f"Teléfono: {cliente['teléfono']}")
    print(f"Correo electrónico: {cliente['correo']}")
    print()

def mostrar_json(objeto):
    cadena_json = json.dumps(objeto, indent=4, ensure_ascii=False)
    print("\nRepresentación JSON de la pizza:")
    print(cadena_json)

def cargar_datos_desde_json(archivo):
    try:
        with open(archivo) as fichero:
            return json.load(fichero)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'")
    except json.decoder.JSONDecodeError:
        print(f"Error: No se pudo leer el archivo '{archivo}' correctamente")

def eliminar_info_vehiculo(datos):
    if "personal" in datos:
        for persona in datos["personal"]:
            persona.pop("vehiculo", None)
    else:
        print("Error: No se encontraron datos de personal en el archivo.")

def guardar_datos_en_json(datos, archivo):
    try:
        with open(archivo, "w") as fichero:
            if datos:
                json.dump(datos, fichero, indent=4, ensure_ascii=False)
                print(f"\nDatos guardados en '{archivo}' correctamente.")
            else:
                print("\nAdvertencia: No hay datos para guardar.")
    except Exception as e:
        print(f"Error al guardar los datos en '{archivo}': {e}")

def menu():
    print("\nMenú:")
    print("1. Mostrar información de la pizza")
    print("2. Mostrar representación JSON de la pizza")
    print("3. Cargar datos desde coches.json")
    print("4. Cargar y guardar datos desde coches.json a personal.json")
    print("5. Salir")

def main():
    pizza = {
        "tamaño": "mediana",
        "precio": 15.90,
        "toppings": ["champiñones", "queso extra", "pepperoni", "albahaca"],
        "cliente": {
            "nombre": "Juan Palomo",
            "teléfono": "666444777",
            "correo": "juanpalomo@meloguisomelocomo.es"
        }
    }

    opcion = None
    while opcion != "5":
        menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            mostrar_informacion_pizza(pizza)
        elif opcion == "2":
            mostrar_json(pizza)
        elif opcion == "3":
            datos_cargados = cargar_datos_desde_json("coches.json")
            if datos_cargados:
                print("\nDatos cargados desde coches.json:")
                for persona in datos_cargados.get("personal", []):
                    print("-" * 20)
                    print(f"Nombre: {persona.get('nombre')}")
                    print(f"Apellido: {persona.get('apellido')}")
                    print(f"Edad: {persona.get('edad')}")
                    print(f"Vehículo: {persona.get('vehiculo')}")
        elif opcion == "4":
            datos_cargados = cargar_datos_desde_json("coches.json")
            if datos_cargados:
                eliminar_info_vehiculo(datos_cargados)
                guardar_datos_en_json(datos_cargados, "personal.json")
        elif opcion == "5":
            print("\nfin...")
        else:
            print("\nOpción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
