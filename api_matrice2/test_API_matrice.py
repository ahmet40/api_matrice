import API_matrice2 as API

def matrice1():
    m1 = API.construit_matrice(3, 4, None)
    API.set_val(m1, 0, 0, 10)
    API.set_val(m1, 0, 1, 11)    
    API.set_val(m1, 0, 2, 12)
    API.set_val(m1, 0, 3, 13)
    API.set_val(m1, 1, 0, 14)
    API.set_val(m1, 1, 1, 15)
    API.set_val(m1, 1, 2, 16)
    API.set_val(m1, 1, 3, 17)
    API.set_val(m1, 2, 0, 18)
    API.set_val(m1, 2, 1, 19)
    API.set_val(m1, 2, 2, 20)
    API.set_val(m1, 2, 3, 21)
    return m1

def matrice2():
    m2 = API.construit_matrice(2, 3, None)
    API.set_val(m2, 0, 0, 'A')
    API.set_val(m2, 0, 1, 'B')    
    API.set_val(m2, 0, 2, 'C')
    API.set_val(m2, 1, 0, 'D')
    API.set_val(m2, 1, 1, 'E')
    API.set_val(m2, 1, 2, 'F')
    return m2

def matrice3():
    m3 = API.construit_matrice(3, 3, None)
    API.set_val(m3, 0, 0, 2)
    API.set_val(m3, 0, 1, 7)    
    API.set_val(m3, 0, 2, 6)
    API.set_val(m3, 1, 0, 9)
    API.set_val(m3, 1, 1, 5)
    API.set_val(m3, 1, 2, 1)
    API.set_val(m3, 2, 0, 4)
    API.set_val(m3, 2, 1, 3)
    API.set_val(m3, 2, 2, 8)
    return m3

def test_get_nb_lignes():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert API.get_nb_lignes(m1) == 3
    assert API.get_nb_lignes(m2) == 2
    assert API.get_nb_lignes(m3) == 3
        


def test_get_nb_colonnes():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert API.get_nb_colonnes(m1) == 4
    assert API.get_nb_colonnes(m2) == 3
    assert API.get_nb_colonnes(m3) == 3

def test_get_val():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert API.get_val(m1, 0, 1) == 11
    assert API.get_val(m1, 2, 1) == 19
    assert API.get_val(m2, 1, 1) == 'E'
    assert API.get_val(m2, 0, 2) == 'C'
    assert API.get_val(m3, 2, 0) == 4
    assert API.get_val(m3, 1, 0) == 9

def test_get_ligne():
    m1 = matrice1()
    assert API.get_ligne(m1,0) == [10,11,12,13]
    assert API.get_ligne(m1,2) == [18,19,20,21]

def test_get_colonne():
    m1 = matrice1()
    assert API.get_colonne(m1,0) == [10,14,18]
    print(API.get_colonne(m1,2))
    
def test_triang_inf():
    m1 = [[1,2,3],[1,0,0],[10,0,1]]
    m2 = [[1,0,0],[1,0,0],[10,0,0]]
    assert API.trian_inf(m1)==False
    assert API.trian_inf(m2) == True
    
def test_triang_sup():
    m1 = [[1,2,3],[1,0,0],[10,0,1]]
    m2 = [[1,20,100],[0,15,20],[0,0,13]]
    assert API.triang_sup(m1)==False
    assert API.triang_sup(m2) == True
    
    
def test_block():
    m1 = [[1,2,3],[1,0,0],[10,0,1]]
    
    assert API.bloc(m1,0,0,1,1)==[[1]]
    assert API.bloc(m1,0,0,2,2)==[[1,2],[1,0]]
    assert API.bloc(m1,0,0,1,2)==[[1,2]]
    
m1 = [[1,2,3],[1,0,0],[10,0,1]]
print(API.bloc(m1,0,0,1,1))


def test_somme():
    m1 = [[1,2,3],[1,0,0],[10,0,1]]
    m2 = [[1,20,100],[0,15,20],[0,0,13]]
    m3 = matrice1()
    assert API.somme(m1,m2) == [[2,22,103],[1,15,20],[10,0,14]]
    assert API.somme(m1,m3) == None
    assert API.somme(m2,m3) == None


def test_produit():
    m1=[[1,2],[3,4]]
    m2=[[1,1],[1,1]]
    assert API.produit(m1,m2) == [[3,3],[7,7]]

m1=[[1,2],[3,4]]
m2=[[1,1],[1,1]]
print(API.produit(m1,m2))
