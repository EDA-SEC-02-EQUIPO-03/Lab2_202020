import pytest
import csv
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

def test_carga():
    lst=[]
    lst=lt.newList()

    file= "Data/GoodReads/books.csv"
    sep=','
    dialect= csv.excel()
    dialect.delimiter = sep

    assert(lt.size(lst)==0),"la lista no empieza en cero"

    try:
        with open(file,encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile,dialect=dialect)

            for row in reader:
                lst.append(row)
                lt.addLast(lst,row)
    except:
        assert False,"Se presento un error al cargar el archivo"
    assert len(lst)== lt.size(lst),"Son diferentes tamaños"

    for i in range (len(lst)):
        assert lt.getElement(lst,i+1)==lst[i],"Las listas no estan en el mismo orden"
