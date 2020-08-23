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
from DataStructures import liststructure as ls

from time import process_time 


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
    lst = lt.newList("SINGLE_LINKED") #Usando implementacion linkedlist
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

    return 

def conocer_a_un_director(nombre, lst1, lst2):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    sum_vote=0
    lstpeli=[]
    iterator2=it.newIterator(lst2)
    iterator1=it.newIterator(lst1)
    while  it.hasNext(iterator2):
        for f in range(1,lst2['size']+1):
            if nombre==lst2['info'][f]["director_name"]:
                id=lst2['info'][f]["id"]
                if id==lst1['info'][f]["id"]:
                    pelicula=lst1['info'][f]["title"]
                    lstpeli[f-1]+=pelicula
                    vote=lst1['info'][f]["vote_average"]
                    sum_vote+=vote
                    cant_vote+=1
    prom= sum_vote/cant_vote
    return [lstpeli,cant_vote,prom]


   # lstpeli=[]
    #for f in range(1,len(lst2)):
      #  if nombre== lst2[f]["director_name"]:
         #   id=lst2[f]["id"] 
          #  if id==lst1[f]["id"]:
           #         pelicula=lst1[f]["title"]
           #         lstpeli[f-1]+=pelicula
           #         vote=lst1[f]["vote_average"]
           #         sum_vote+=vote
           #         cant_vote+=1
   # num_pelis=len(lstpeli)
    #prom= sum_vote/cant_vote
   # return (lstpeli,num_pelis,prom)
    
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()  # se require usar lista definida
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada 
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista = loadCSVFile("Data\theMoviesdb\SmallMoviesDetailsCleaned") #llamar funcion cargar datos
                print("Datos cargados, ",lista['size']," elementos cargados")
                #lista2 = loadCSVFile("Data\theMoviesdb\MoviesCastingRaw-small") #llamar funcion cargar datos
                #print("Datos cargados, ",lista2['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista1) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista1==None or lista1['size']==0: #obtener la longitud de la lista
                    print("La lista del archivo 1 esta vacía")
                if lista2==None or lista2['size']==0: #obtener la longitud de la lista
                    print("La lista del archivo 2 esta vacía")
                else:
                    nombre =input('Ingrese el nombre del director que desea consultar\n')
                    director=conocer_a_un_director(nombre, lista1, lista2)

                    print("El director",nombre,"tiene", director[1] ,"peliculas que ha dirigido,\n"
                            " con un promedio de calificación de ",director[2])
                    print("Las peliculas dirigidas por el director son:")
                    for i in director[0]:
                        print(i)
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()