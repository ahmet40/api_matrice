""" Matrices : API n 1 """


def construit_matrice(nb_lignes, nb_colonnes, valeur_par_defaut):
    """crée une nouvelle matrice en mettant la valeur par défaut dans chacune de ses cases.

    Args:
        nb_lignes (int): le nombre de lignes de la matrice
        nb_colonnes (int): le nombre de colonnes de la matrice
        valeur_par_defaut : La valeur que prendra chacun des éléments de la matrice

    Returns:
        une nouvelle matrice qui contient la valeur par défaut dans chacune de ses cases
    """
    matrice= (nb_lignes,nb_colonnes,[])
    for i in range(nb_colonnes*nb_lignes):
        matrice[2].append(valeur_par_defaut)
    return matrice




def set_val(matrice, ligne, colonne, nouvelle_valeur):
    """permet de modifier la valeur de l'élément qui se trouve à la ligne et à la colonne
    spécifiées. Cet élément prend alors la valeur nouvelle_valeur

    Args:
        matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)
        nouvelle_valeur : la nouvelle valeur que l'on veut mettre dans la case

    Returns:
        None
    """
    matrice[2][ligne*matrice[1]+colonne] = nouvelle_valeur


def get_nb_lignes(matrice):
    """permet de connaître le nombre de lignes d'une matrice

    Args:
        matrice : une matrice

    Returns:
        int : le nombre de lignes de la matrice
    """
    return matrice[0]


def get_nb_colonnes(matrice):
    """permet de connaître le nombre de colonnes d'une matrice

    Args:
        matrice : une matrice

    Returns:
        int : le nombre de colonnes de la matrice
    """
    return matrice[1]


def get_val(matrice, ligne, colonne):
    """permet de connaître la valeur de l'élément de la matrice dont on connaît
    le numéro de ligne et le numéro de colonne.

    Args:
        matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)

    Returns:
        la valeur qui est dans la case située à la ligne et la colonne spécifiées
    """
    return matrice[2][ligne*matrice[1]+colonne]

# Fonctions pour l'affichage 

def affiche_ligne_separatrice(matrice, taille_cellule=4):
    """fonction auxilliaire qui permet d'afficher (dans le terminal)
    une ligne séparatrice

    Args:
        matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    print()
    for _ in range(get_nb_colonnes(matrice) + 1):
        print('-'*taille_cellule+'+', end='')
    print()


def affiche(matrice, taille_cellule=4):
    """permet d'afficher une matrice dans le terminal

    Args:
        matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    nb_colonnes = get_nb_colonnes(matrice)
    nb_lignes = get_nb_lignes(matrice)
    print(' '*taille_cellule+'|', end='')
    for i in range(nb_colonnes):
        print(str(i).center(taille_cellule) + '|', end='')
    affiche_ligne_separatrice(matrice, taille_cellule)
    for i in range(nb_lignes):
        print(str(i).rjust(taille_cellule) + '|', end='')
        for j in range(nb_colonnes):
            print(str(get_val(matrice, i, j)).rjust(taille_cellule) + '|', end='')
        affiche_ligne_separatrice(matrice, taille_cellule)
    print()


# Ajouter ici les fonctions supplémentaires, sans oublier de compléter le fichier
# tests_API_matrice.py avec des fonctions de tests





#--------------------------------
#VERSION NUMERO 2 DES MATRICE EXO 5
#--------------------------------

def get_ligne(matrice,ligne):
    """
        Fonction qui renvoie une ligne de matrice donne en parametre
        Args:
            entrer:
                matrice(tuple): nombre ligne, nombre colonne, matrice
                ligne(int): un numero de ligne demandé
            return :
                une liste qui contient les valeurs de la ligne.
    """
    if ligne<matrice[0]:
        return matrice[2][matrice[1]*ligne :matrice[1]*ligne+matrice[1]]  #on prend la liste de valeur jusqu'à la fin de la ligne


def get_colonne(matrice,colonne):
    """
        Fonction qui renvoie les valeurs d'une colonne de matrice donné en paramètre
        Args:
            entrer:
                matrice(tuple): nombre ligne, nombre colonne, matrice
                colonne(int): un numero de ligne demandé
            return :
                une liste qui contient les valeurs de la colonne.
    """
    if colonne < matrice[1]:
        liste_colonne=[]
        for chiffre in range(colonne,len(matrice[2]),matrice[1]):       #on parcour la liste de la colonne avec des pas qui nous donne l'indice de la valeur de la colonne
            liste_colonne.append(matrice[2][chiffre])
        return liste_colonne


def get_diagonale_principale(matrice):
    """
        Fonction qui renvoie la diagonale d'une matrice donnée en paramètre
        Args:
            entrer:
                matrice(tuple): nombre ligne, nombre colonne, matrice
                
            return :
                une liste qui contient les valeurs de la diagonale.
    """
    if matrice[1] == matrice[0]:                #verifie que c'est une matrice carré
        liste_diagonal=[]
        
        for numero_colonne in range(0,len(matrice[2]),matrice[1]+1):        #parcoure la matrice et saute du nombre de colonne +1 pour avoir le chiffre suivant dans la matrice
            liste_diagonal.append(matrice[2][numero_colonne])
        return liste_diagonal
    return "votre matrice n'est pas carre"


def get_diagonale_secondaire(matrice):
    """
        Fonction qui renvoila diagonale secondaire d'une matrice donnéz en paramètre
        Args:
            entrer:
                matrice(tuple): nombre ligne, nombre colonne, matrice
                
            return :
                une liste qui contient les valeurs de la diagonale secondaire.
    """
    if matrice[1] == matrice[0]:
        diagonale_secondaire=[]
        for numero_colonne in range(matrice[1]-1,len(matrice[2])-1,matrice[1]-1):  
            #parcoure la matrice et saute du nombre de colonne -1 pour avoir le chiffre suivant dans la matrice et va jusqu'a len -1 pour ne pas avoir le dernier chiffre
            diagonale_secondaire.append(matrice[2][numero_colonne])
        return diagonale_secondaire
    return "votre matrice n'est pas carre"


def transpose(matrice):
    """
        Fonction qui renvoi la matrice donné tel que les lignes sont devenus des colonnes
        Args:
            entrer:
                matrice(tuple): nombre ligne, nombre colonne, matrice
                
            return :
                matrice(tuple): nombre ligne, nombre colonne, matrice inversé
    """
    if matrice[1] == matrice[0]:
        liste_renvoye=[]
        liste_de_colonne=[]
        for nombre_colonne in range(matrice[1]):
            liste_de_colonne.append(get_colonne(matrice,nombre_colonne))        #ajoute les listes de colonnes dans une liste 
        for element in liste_de_colonne:                    
            for element_colonne in element:
                liste_renvoye.append(element_colonne)
        return (matrice[0],matrice[1],liste_renvoye)
    return "votre matrice n'est pas carre"


def is_triangulaire_inf(matrice):
    """
        Fonction qui verifie que la matrice donnée est triangulaire inférieur (les valeurs au-dessus de la diagonale doivent etre à 0)
        Args:
            entrer:
                matrice(tuple): nombre ligne, nombre colonne, matrice
                
            return :
                bool: indice si la matrice est triangulaire inférieur
    """
    if matrice[1] == matrice[0]:
        for colonne in range(matrice[1]):
            liste_colonne=get_colonne(matrice,colonne)
            for valeur in range(colonne): # prend les valeur du début jusq'à la diagonal 
                if liste_colonne[valeur] != 0:
                    return False
        return True
    print("je suis inferieur")