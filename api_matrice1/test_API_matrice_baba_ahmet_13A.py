""" tests pour les API matrices 
    Remarques : tous les tests de ce fichier doivent passer quelle que soit l'API utilisée
    """
import API_matrice1_baba_ahmet_13A as API

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


def matrice4():
    m4 = API.construit_matrice(2,2, None)
    API.set_val(m4, 0, 0, 2)
    API.set_val(m4, 0, 1, 0)    
    API.set_val(m4, 1, 0, 9)
    API.set_val(m4, 1, 1, 5)
    return m4



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



#--------------------------------
# TEST Matrice exo 5
#--------------------------------



def test_get_ligne():
    matrice = matrice2()
    assert API.get_ligne(matrice,1) == ['D','E','F']       # le 1 est faite pour la ligne numero 2 car on commence à compter les lignes de la matrice à 0.

test_get_ligne()


def test_get_colonne():
    matrice = matrice2()
    assert API.get_colonne(matrice,1) == ['B','E']

test_get_colonne()  

def test_diagonal():
    assert API.get_diagonale_principale(matrice3()) == [2, 5, 8]

test_diagonal()

def test_diagonal_secondaire():
    assert API.get_diagonale_secondaire(matrice3()) ==[6, 5, 4]

test_diagonal_secondaire()

m5=(3,3,[1,2,3,4,5,6,7,8,9])

def test_is_triangulaire_inferieur():
    assert API.is_triangulaire_inf(matrice4()) == True
    assert API.is_triangulaire_inf(m5) == False

test_is_triangulaire_inferieur()


def test_transpose():
    assert API.transpose(matrice3()) == (3,3,[2, 9, 4, 7, 5, 3, 6, 1, 8])

test_transpose()



m6=(3,3,[1,2,3,4,0,3,10,9,8])
m7=(3,3,[1,2,3,0,5,6,0,0,9])
m8=(2,3,[1,2,3,0,5,6])
m9=(2,2,[1,2,3,4])


def test_is_triang_sup():
    assert API.is_triang_sup(m6) == False
    assert API.is_triang_sup(m7) == True

print(API.is_triang_sup(m6))

def test_somme():
    assert API.somme(m6,m7) == (3,3,[2,4,6,4,5,9,10,9,17])
    assert API.somme(m8,m9) == None



def test_block():
    m1 = (3,3,[1,2,3,1,0,0,10,0,1])
    
    assert API.bloc(m1,0,0,1,1)==(1,1,[1])
    assert API.bloc(m1,0,0,2,2)==(2,2,[1,2,1,0])
    assert API.bloc(m1,0,0,1,2)==(1,2,[1,2])
    
m1 = (3,3,[1,2,3,1,0,0,10,0,1])
print(API.bloc(m1,0,0,1,1))


def test_somme():
    m1 = (3,3,[1,2,3,1,0,0,10,0,1])
    m2 = (3,3,[1,20,100,0,15,20,0,0,13])
    m3 = matrice1()
    assert API.somme(m1,m2) == (3,3,[2,22,103,1,15,20,10,0,14])
    assert API.somme(m1,m3) == None
    assert API.somme(m2,m3) == None


def test_produit():
    m1=(2,2,[1,2,3,4])
    m2=(2,2,[1,1,1,1])
    assert API.produit(m1,m2) == (2,2,[3,3,7,7])

