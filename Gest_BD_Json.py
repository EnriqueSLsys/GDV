#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error
import json
import getpass
import argparse

def establecerConexion(servidor, usuario, password, bd=None):
    conexion = None
    try:
        conexion = mysql.connector.connect(
            host=servidor,
            user=usuario,
            passwd=password,
            database=bd
        )
        print("Conexión establecida")
    except Error as err:
        print(f"Error: '{err}'")
    return conexion

def creaBaseDeDatos(sesion, nombre_bd):
    cursor = sesion.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre_bd}")
        print(f"Base de datos '{nombre_bd}' creada correctamente")
    except Error as err:
        print(f"Error: '{err}'")

def creaTablaVehiculos(conexion):
    cursor = conexion.cursor()
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS vehiculos (id INT AUTO_INCREMENT PRIMARY KEY, marca VARCHAR(255), modelo VARCHAR(255), año INT, color VARCHAR(255), tipo_combustible VARCHAR(255), cilindraje INT, matricula VARCHAR(255))")
        print("Tabla 'vehiculos' creada correctamente")
    except Error as err:
        print(f"Error: '{err}'")

def ejecutaSQL(conexion, orden, valores=None):
    cursor = conexion.cursor()
    try:
        if valores:
            cursor.executemany(orden, valores)  # Utilizamos executemany para insertar múltiples filas
        else:
            cursor.execute(orden)
        conexion.commit()
        print("Orden ejecutada correctamente")
    except Error as err:
        print(f"Error: '{err}'")

def cargarDatosDesdeJSON(archivo):
    try:
        with open(archivo) as fichero:
            return json.load(fichero)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'")
    except json.decoder.JSONDecodeError:
        print(f"Error: No se pudo leer el archivo '{archivo}' correctamente")

def mostrarTabla(conexion):
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT * FROM vehiculos")
        filas = cursor.fetchall()
        print("Tabla 'vehiculos':")
        for fila in filas:
            print(fila)
    except Error as err:
        print(f"Error: '{err}'")

def main(servidor, usuario, password, nombre_bd):  # Agrega usuario y password como argumentos
    sesion = establecerConexion(servidor, usuario, password, nombre_bd)

    if sesion:
        creaBaseDeDatos(sesion, nombre_bd)
        creaTablaVehiculos(sesion)

        # Cargar datos desde un archivo JSON
        datos_json = cargarDatosDesdeJSON("datos.json")
        if datos_json:
            # Insertar datos en la tabla 'vehiculos'
            orden = "INSERT INTO vehiculos (marca, modelo, año, color, tipo_combustible, cilindraje, matricula) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            valores = [(item['marca'], item['modelo'], item['año'], item['color'], item['tipo_combustible'], item['cilindraje'], item['matricula']) for item in datos_json]
            ejecutaSQL(sesion, orden, valores)

        # Mostrar la tabla 'vehiculos'
        mostrarTabla(sesion)

        sesion.close()
        print("Conexión cerrada")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script para manejar información de vehículos en una base de datos MySQL")
    parser.add_argument("servidor", type=str, help="Dirección del servidor MySQL")
    parser.add_argument("--bd", type=str, help="Nombre de la base de datos MySQL")
    args = parser.parse_args()

    usuario = input("Ingrese el nombre de usuario de MySQL: ")
    password = getpass.getpass("Ingrese la contraseña de MySQL: ")

    main(args.servidor, usuario, password, args.bd)  # Pasa usuario y contraseña como argumentos
