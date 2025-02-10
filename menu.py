import os
from listas import *
from tabulate import tabulate

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_en_tabla(lista):
    if isinstance(lista, ListaContigua) or isinstance(lista, ListaIndexada):
        datos = [[i+1, elemento] for i, elemento in enumerate(lista.lista)]
    else:
        datos = []
        actual = lista.cabeza
        index = 1
        while actual:
            datos.append([index, actual.dato])
            actual = actual.siguiente
            index += 1
    
    if datos:
        print(tabulate(datos, headers=["Índice", "Valor"], tablefmt="grid"))
    else:
        print("La lista está vacía.")

def submenu(lista):
    while True:
        limpiar_pantalla()
        print("Seleccione una acción:")
        print("1. Insertar datos")
        print("2. Eliminar datos")
        print("3. Mostrar datos")
        print("4. Regresar al menú principal")
        opcion = input("Ingrese una opción: ")
        
        if opcion == '1':
            elemento = input("Ingrese un elemento: ")
            lista.insertar(elemento)
        elif opcion == '2':
            mostrar_en_tabla(lista)
            elemento = input("Ingrese el elemento a eliminar: ")
            lista.eliminar(elemento)
        elif opcion == '3':
            mostrar_en_tabla(lista)
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Intente nuevamente.")
        input("Presione Enter para continuar...")

def menu_principal():
    lista_contigua = ListaContigua()
    lista_ligada = ListaLigada()
    lista_doblemente_ligada = ListaDoblementeLigada()
    lista_indexada = ListaIndexada()
    
    while True:
        limpiar_pantalla()
        print("Seleccione el tipo de lista a probar:")
        print("1. Lista Contigua (Arreglo)")
        print("2. Lista Ligada (Simple)")
        print("3. Lista Doblemente Ligada")
        print("4. Lista Indexada")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")
        
        if opcion == '1':
            submenu(lista_contigua)
        elif opcion == '2':
            submenu(lista_ligada)
        elif opcion == '3':
            submenu(lista_doblemente_ligada)
        elif opcion == '4':
            submenu(lista_indexada)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
        input("Presione Enter para continuar...")
