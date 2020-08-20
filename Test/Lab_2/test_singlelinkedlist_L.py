import pytest
import csv
from DataStructures import linkedlistiterator as it
from DataStructures import singlelinkedlist as lst

def test_carga():
    List =[]
    List_ADT= lst.newList()
    
    file= 'Data/theMoviesdb/AllMoviesCastingRaw.csv'
    sep=';'
    dialect= csv.excel()
    dialect.delimiter=sep
    
    assert(lst.size(List_ADT)==0), "La lista no empieza en cero"
   
    try:
        with open(file,encoding='utf-8') as csvfile:
            reader=csv.DictReader(csvfile, dialect=dialect )

            for row in reader:
                List.append(row)
                lst.addLast(List_ADT,row)
    except:
        assert False,'Se presentó un error al cargar el archivo'
   
    assert len(List) == lst.size(List_ADT), 'Son de distionto tamaño'

    for x in range(len(List)):
        assert lst.getElement(List_ADT,x+1)==List[x], 'Las listas no estan en el mismo orden'