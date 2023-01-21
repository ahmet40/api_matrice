#import API_matrice1_baba_ahmet_13A as API
import API_matrice2_baba_ahmet_13A as API



def construit_matrice(ligne,colonne,valeur_par_defaut=0):
    return API.construit_matrice(ligne,colonne,valeur_par_defaut)

def get_nb_lignes(matrice):
    return API.get_nb_lignes(matrice)

def get_nb_colonnes(matrice):
    return API.get_nb_colonnes(matrice)

def get_val(matrice,ligne,colonne):
    return API.get_val(matrice,ligne,colonne)

def set_val(matrice,ligne,colonne,nouvelle_valeur):
    return API.set_val(matrice,ligne,colonne,nouvelle_valeur)

def get_ligne(matrice,ligne):
    return API.get_ligne(matrice,ligne)

def get_colonne(matrice,colonne):
    return API.get_colonne(matrice,colonne)

def get_diagonale_principale(matrice):
    return API.get_diagonale_principale(matrice)

def get_diagonale_secondaire(matrice):
    return API.get_diagonale_secondaire(matrice)

def transpose(matrice):
    return API.transpose(matrice)

def is_triangulaire_inf(matrice):
    return API.is_triangulaire_inf(matrice)

def is_triangulaire_sup(matrice):
    """
	Cette fonction vous dit si la matrice donné est traingulaire superieur ou non
	Args:
		entrer:
			Matrice une liste de liste.
		sortie:
			bool
    """
    return is_triangulaire_inf(transpose(matrice))

def bloc(matrice,ligne,colonne,hauteur,largeur):
    """Cette fonction renvoi le block à partir de la valeur au ligne et colonne donne 
        Args:
            entrer:
                matrice: list de list
                ligne: int
                colonne: int
                hauteur: int
                largeur:int
            sortie:
                une liste de liste
    """
    matrice_a_renvoye = construit_matrice(hauteur, largeur, None)
    nb_ligne=get_nb_lignes(matrice)
    nb_colonne=get_nb_colonnes(matrice)
    liste=[]
    if ligne + hauteur < nb_ligne and colonne+largeur < nb_colonne:         #verifie qu'on ne sort pas la matrice
        while ligne < hauteur:
            liste.append(get_ligne(matrice,ligne)[colonne:largeur])
            for valeur in range(len(liste[ligne])):
                set_val(matrice_a_renvoye,ligne,valeur,liste[ligne][valeur])
            ligne+=1
        return matrice_a_renvoye
            
    
def somme (matrice1,matrice2):
    """
    Fonction qui fait la somme des deux matrices données en paramétre.
    Args:
		entrer:
			Matrice1 une liste de liste.
            Matrice1 une liste de liste.
		sortie:
			une matrice qui a fait la somme des matrices données en parametre
    """
    if get_nb_colonnes(matrice1) == get_nb_colonnes(matrice2) and get_nb_lignes(matrice1) == get_nb_lignes(matrice2):
        #cree des sous listes dans lequel il ajoute les valeur de la matrice 1 avec celui de la matrice 2 pour chaque colonne dans les sous listes
        #il ajoute ces suous listes dans une grande liste qui sera notre matrice
        matrice_a_renvoye = construit_matrice(get_nb_lignes(matrice1), get_nb_colonnes(matrice1), None) #construit la matrice a reenvoye
        for ligne in range(get_nb_lignes(matrice1)): #parcour par indice des lignes
            m1_ligne=get_ligne(matrice1,ligne)       #prend la ligne de la matrice 1
            m2_ligne=get_ligne(matrice2,ligne)       #prend la ligne de la matrice 2
            for valeur in range(len(m1_ligne)):
                valeur_a_remplcer=m1_ligne[valeur]+m2_ligne[valeur]
                set_val(matrice_a_renvoye, ligne, valeur, valeur_a_remplcer)        #remplace la valeur de la matrice a renvoye par sa nouvelle valeur
        return matrice_a_renvoye
    return "somme impossible"

                


def produit(matrice1,matrice2):
    """
    Fonction qui fait le produit des deux matrices données en paramétre.
    Args:
		entrer:
			Matrice1 une liste de liste.
            Matrice1 une liste de liste.
		sortie:
			une matrice qui a fait le produit des matrices données en parametre
    """
    if get_nb_colonnes(matrice2) == get_nb_lignes(matrice1):        #verifie que nous pouvons faire le produit des deux matrices
        matrice_a_renvoye = construit_matrice(get_nb_lignes(matrice1), get_nb_colonnes(matrice1), None)
        for ligne in range(get_nb_lignes(matrice1)):                      #parcourt la liste et donne les indices des sous-listes
            liste=[]
            for colonne in range(get_nb_colonnes(matrice1)):         #donne l'indice de la colonne
                val=0
                liste_colonne=get_colonne(matrice2,colonne)     #prend la colonne qu'il faut multiplier
                liste_ligne=get_ligne(matrice1,ligne)           #prend la ligne qu'il faut multiplier
                for valeur in range(len(liste_colonne)):        #parcourt par indice des valeurs des colonnes et lignes
                    val+=liste_colonne[valeur]*liste_ligne[valeur]      # multiplie les valeurs des lignes et des colonnes pour obtenir le resultat
                    set_val(matrice_a_renvoye,ligne,colonne,val) 
                liste.append(val)
        return matrice_a_renvoye
    return "produit impossible"








#--------------------------------------------------------------------------------
# Les Test
#--------------------------------------------------------------------------------



"""
matrice=construit_matrice(3,3)
matrice2=construit_matrice(3,3)

set_val(matrice,0,1,15)



set_val(matrice2,0,0,1)
set_val(matrice2,0,1,2)
set_val(matrice2,0,2,3)
set_val(matrice2,1,0,4)
set_val(matrice2,1,1,5)
set_val(matrice2,1,2,6)
set_val(matrice2,2,0,7)
set_val(matrice2,2,1,8)
set_val(matrice2,2,2,9)



print("la matrice 1 a: {} lignes".format(get_nb_lignes(matrice)) ,"\n")

print("la matrice 1 a: {} colonnes".format(get_nb_colonnes(matrice)))
print("la valeur à la ligne 0 et colonne 1 de la matrice 1 est; {}".format(get_val(matrice,0,1)),"\n")
print("la ligne 0 de la matrice 1 est: {}".format(get_ligne(matrice,0)),"\n")
print("la colonne 0 de la matrice 1 est: {}".format(get_colonne(matrice,0)),"\n")
print("diagonal principale de la matrice1: {}".format(get_diagonale_principale(matrice)),"\n")
print("diagonal secondaire de la matrice1: {}".format(get_diagonale_secondaire(matrice)),"\n")
print("transpose matrice1:{}".format(transpose(matrice)),"\n")
print("la matrice 1 est triangulaire inferieur: {}".format(is_triangulaire_inf(matrice)),"\n")
print("la matrice 2 est triangulaire inferieur: {}".format(is_triangulaire_inf(matrice2)),"\n")
print("triangulaire sur 1: {}".format(is_triangulaire_sup(matrice)),"\n")
print("triangulaire sur 2: {}".format(is_triangulaire_sup(matrice2)),"\n")
print(bloc(matrice2,0,0,2,2),"\n")
print(somme(matrice,matrice2),"\n")
print(matrice,matrice2,produit(matrice,matrice2))
"""

m=[[1,2,3]]
m2=[[1,2,3]]
print(produit(m,m2))