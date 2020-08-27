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
    e="linkedlist"
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = lt.newIterator(e,lst)
        while  lt.iterator_hasnext(e,iterator):
            element = lt.next(e,iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter


def countElementsByCriteria(criteria,lista1,lista2):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    e="linkedlist"
    t1_start = process_time()
    lstpeli=[]
    sum_vote=0
    cant_vote=0
    for i in range(1,lt.size(lista1)+1):
                    valor1=lt.getElement(lista1,i)
                    valor2=lt.getElement(lista2,i)
                    n=valor2['director_name']
                    if criteria==n:
                        pelicula=valor1["original_title"]
                        lstpeli.append(pelicula)
                        vote=valor1["vote_average"]
                        sum_vote+=float(vote)
                        cant_vote+=1     
    num_pelis=len(lstpeli)
    prom= sum_vote/cant_vote
    t1_stop = process_time() 
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return [lstpeli,num_pelis,prom]



def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista1 = lt.newList()
    lista2 = lt.newList()# se require usar lista definida
    while True:
            printMenu() #imprimir el menu de opciones en consola
            inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada 
            if len(inputs)>0:
                if int(inputs[0])==1:
                    lista1 = loadCSVFile("Data/theMoviesdb/SmallMoviesDetailsCleaned.csv") 
                    lista2 = loadCSVFile("Data/theMoviesdb/MoviesCastingRaw-small.csv") 
                    #llamar funcion cargar datos
                    print("Datos cargados, ",lt.size(lista1)," elementos cargados")
                    print("Datos cargados, ",lt.size(lista2)," elementos cargados")
                    #llamar funcion cargar datos
                    #print("Datos cargados, ",lista2['size']," elementos cargados")
                elif int(inputs[0])==2: #opcion2
                    if lista1==None or lt.size(lista1)==0: #obtener la longitud de la lista
                        print("La lista esta vacía")    
                    else: print("La lista tiene ",lt.size(lista1)," elementos")
                    if lista2==None or lt.size(lista2)==0: #obtener la longitud de la lista
                        print("La lista esta vacía")    
                    else: print("La lista tiene ",lt.size(lista2)," elementos")
                elif int(inputs[0])==3: #opcion 3
                    if lista1==None or lt.size(lista1)==0: #obtener la longitud de la lista
                        print("La lista esta vacía")
                    else:   
                        criteria =input('Ingrese el criterio de búsqueda\n')
                        counter=countElementsFilteredByColumn(criteria, "nombre", lista1) #filtrar una columna por criterio  
                        print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
                elif int(inputs[0])==4: #opcion 4
                    if lista1==None or lt.size(lista1)==0: #obtener la longitud de la lista
                        print("La lista del archivo 1 esta vacía")
                    if lista2==None or lt.size(lista2)==0: #obtener la longitud de la lista
                        print("La lista del archivo 2 esta vacía")
                    else:
                        criteria =input('Ingrese el director que quiere buscar\n')
                        counter=countElementsByCriteria(criteria,lista1,lista2)
                        print("Las peliculas del director ",criteria,"son ",counter[1]," las cuales se nombraran en el siguiente listado:")
                        for k in counter[0]:
                            print(k)
                        print("Las anteriores tienen un promedio de votación de: ",counter[2])
                elif int(inputs[0])==0: #opcion 0, salir
                    sys.exit(0)
                
if __name__ == "__main__":
    main()