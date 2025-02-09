import os
from listas import *

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

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
            elemento = input("Ingrese un elemento: ")
            lista_contigua.insertar(elemento)
            lista_contigua.mostrar()
        elif opcion == '2':
            elemento = input("Ingrese un elemento: ")
            lista_ligada.insertar(elemento)
            lista_ligada.mostrar()
        elif opcion == '3':
            elemento = input("Ingrese un elemento: ")
            lista_doblemente_ligada.insertar(elemento)
            lista_doblemente_ligada.mostrar()
        elif opcion == '4':
            elemento = input("Ingrese un elemento: ")
            lista_indexada.insertar(elemento)
            lista_indexada.mostrar()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
        input("Presione Enter para continuar...")