import pytest
import csv
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

def test_carga():
    lista=[]
    lst=lt.newList()

    file= "Data/Good reads descarga/books-small.csv"
    sep=','
    dialect= csv.excel()
    dialect.delimiter = sep

assert(lt.size(lst)==0),"la lista no empieza en cero"

try:
    with open(file,encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile,dialect=dialect)

        for row in reader:
            lista.append(row)
            lt.addLast(lst,row)
except:
    assert False,"Se presento un error al cargar el archivo"
assert len(lista)== lt.size(lst),"Son diferentes tamaños"

for i in range (len(lista)):
    assert lt.getElement(lst,i+1)==lista[i],"Las listas no estan en el mismo orden"
