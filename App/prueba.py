import csv
from DataStructures import listiterator as it
from DataStructures import liststructuren as lt

def test_carga():
    lista=[]
    lst = lt.newList()

    file='Data/test.csv'
    sep=','
    dialect= csv.excel()
    dialect.delimiter = sep

    try:
        with open(file,encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile,dialect=dialect)

            for row in reader:
                lista.append(row)
                lt.addLast(lst,row)
    except:
        print("Se presento un error al cargar los archivos")
    print("Lista python")
    for i in lista:
        print(i)

    print("Lista de DTA")
    iterator=it.newIterator(lst)
    while it.hasNext(iterator):
        element= it.next(iterator)
        print(element)
test_carga()

