import config
import pytest
import csv
from ADT import list as lst
list_type = 'SINGLELINKED_LIST'
def test_carga():
    List =[]
    List_ADT= lst.newList(list_type)
    
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
def cmpfunction (element1, element2):
    if element1["id"] == element2["id"]:
        return 0
    elif element1["id"] < element2["id"]:
        return -1
    else:
        return 1

@pytest.fixture
def slt ():
    slt = lst.newList(list_type)
    return slt


@pytest.fixture
def movies ():
    movies = []
    movies.append({'id':'1', 'title':'Title 1', 'author':'author 1'})
    movies.append({'id':'2', 'title':'Title 2', 'author':'author 2'})
    movies.append({'id':'3', 'title':'Title 3', 'author':'author 3'})
    movies.append({'id':'4', 'title':'Title 4', 'author':'author 4'})
    movies.append({'id':'5', 'title':'Title 5', 'author':'author 5'})
    print (movies[0])
    return movies


@pytest.fixture
def lstmovies(movies):
    slt = lst.newList(list_type,cmpfunction)
    for i in range(0,5):    
        lst.addLast(slt,movies[i])    
    return slt

def test_empty (slt):
    assert lst.isEmpty(slt) == True
    assert lst.size(slt) == 0

def test_addLast (slt, movies):
    assert lst.isEmpty(slt) == True
    assert lst.size(slt) == 0
    lst.addLast (slt, movies[0])
    assert lst.size(slt) == 1
    lst.addLast (slt, movies[1])
    assert lst.size(slt) == 2
    movie = lst.firstElement(slt)
    assert movie == movies[0]
    movie = lst.lastElement(slt)
    assert movie == movies[1]

    
def test_getElement(lstmovies, movies):
    movie = lst.getElement(lstmovies, 1)
    assert movie == movies[0]
    movie = lst.getElement(lstmovies, 5)
    assert movie == movies[4]





def test_removeFirst (lstmovies, movies):
    assert lst.size(lstmovies) == 5
    lst.removeFirst(lstmovies)
    assert lst.size(lstmovies) == 4
    movie = lst.getElement(lstmovies, 1)
    assert movie  == movies[1]



def test_removeLast (lstmovies, movies):
    assert lst.size(lstmovies) == 5
    lst.removeLast(lstmovies)
    assert lst.size(lstmovies) == 4
    movie = lst.getElement(lstmovies, 4)
    assert movie  == movies[3]



def test_insertElement (slt, movies):
    assert lst.isEmpty(slt) is True
    assert lst.size(slt) == 0
    lst.insertElement (slt, movies[0], 1)
    assert lst.size(slt) == 1
    lst.insertElement (slt, movies[1], 2)
    assert lst.size(slt) == 2
    lst.insertElement (slt, movies[2], 1)
    assert lst.size(slt) == 3
    movie = lst.getElement(slt, 1)
    assert movie == movies[2]
    movie = lst.getElement(slt, 2)
    assert movie == movies[0]



def test_isPresent (lstmovies, movies):
    book = {'id':'10', 'title':'Title 10', 'author':'author 10'}
    print(lst.isPresent (lstmovies, movies[2]))
    assert lst.isPresent (lstmovies, movies[2]) > 0
    assert lst.isPresent (lstmovies, movies) == 0
    


def test_deleteElement (lstmovies, movies):
    pos = lst.isPresent (lstmovies, movies[2])
    assert pos > 0
    movie = lst.getElement(lstmovies, pos)
    assert movie == movies[2]
    lst.deleteElement (lstmovies, pos)
    assert lst.size(lstmovies) == 4
    movie = lst.getElement(lstmovies, pos)
    assert movie == movies[3]


def test_changeInfo (lstmovies):
    movie10 = {'id':'10', 'title':'Title 10', 'author':'author 10'}
    lst.changeInfo (lstmovies, 1, movie10)
    movie = lst.getElement(lstmovies, 1)
    assert movie10 == movie


def test_exchange (lstmovies, movies):
    movie1 = lst.getElement(lstmovies, 1)
    movie5 = lst.getElement(lstmovies, 5)
    lst.exchange (lstmovies, 1, 5)
    assert lst.getElement(lstmovies, 1) == movie5
    assert lst.getElement(lstmovies, 5) == movie1
    