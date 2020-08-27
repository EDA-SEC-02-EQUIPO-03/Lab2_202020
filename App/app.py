"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import insertionsort as ins
from Sorting import selectionsort as sel

from time import process_time 

def less(element1, element2,condition):1
    if float(element1[condition]) < float(element2[condition]):
        return True
    return False

def greater(element1, element2,condition):
    if float(element1[condition]) > float(element2[condition]):
        return True
    return False

def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0

def orderElementsByCriteria(lst, rank, parameter, orden):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    tempo=lt.newList() #list donde se almacena la lista desordenada con puntuaciones y nombres
    final=[] #list donde se almacena la lista ordenada de nombres
    p='vote_average' #criterio de de puntuacion
    o=less #sentido de la lista
    d='WORST ' #prefijo para el print



    if orden.lower() == 'ascendente': #definir orden
        o=greater
        d='BEST'
    if parameter.lower() == 'count': #definir criterio
        p='vote_count'


    for i in range(0,lt.size(lst)):
        for j in range(len(rank)):
            elemento=lt.getElement(lst,i)
            if elemento["original_title"]==rank[j]:        
                lt.addLast(tempo,elemento) #añadir puntuacion y nombre en desorden
    
    tempo=ins.insertionSort(tempo,o,p)
    print(tempo)
    for k in range(len(tempo)):
        final.append(tempo[k][1]) #añadir nombres ordenados a la lista
    print('Top ',len(final),' ',d,'',parameter,': \n',final) #impresion final de los datos con la lista, el largo de la lista y los parametros de orden
    return 0


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista1= lt.newList()
    lista2=lt.newList()
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista1 = loadCSVFile("Data/thMoviesdb/SmallMoviesDetailsCleaned.csv") #llamar funcion cargar datos
                print("Datos cargados, ",lista1['size']," elementos cargados")
                lista2 = loadCSVFile("Data/thMoviesdb/MoviesCastingRaw-small.csv")
                print("Datos cargados, ",lista2['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if lista1==None or lista1['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista1['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if lista1==None or lista1['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=orderElementsByCriteria(lista,['The Dark','The Fifth Element','Todo sobre mi madre','Back to the Future','Dracula','Back to the Future Part II','The Wizard','The King of Comedy','Fargo','Terminator 2: Judgment Day',"Dave Chappelle's Block Party",'Rio Bravo','Alien'],'COUNT','descendente')
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()