from copy import copy

# On va programmer un petit jeu
# La position dans le jeu est une liste croissante comme
# [1,2,3,4]
# [5,8,8,8]
# [0,0,0,0]
# l est croissante si l[i] <= l[i+1] pour tout i entre 0 et len(l) - 2

# Un coup consiste à choisir un des entiers de la liste et à le diminuer
# de un ou plus, mais la liste doit rester croissante.

# Par exemple si on part de la position [5,8,8,8] on peut atteindre
# les positions suivantes:
# [4,8,8,8]
# [3,8,8,8]
# [2,8,8,8]
# [1,8,8,8]
# [0,8,8,8]
# [5,7,8,8]
# [5,6,8,8]
# [5,5,8,8]

# Le premier joueur qui ne peut plus jouer à perdu.

# Question 1: quelle est la seule position qui est perdante (on ne peut pas jouer)
# si on joue avec une liste de taille 4 ?
position_perdante_4 = []

# Lisez la fonction suivante
def coups_possibles(position):
    """prend une position en entrée et retourne la liste des coups
    possibles. Chaque coups est un couple (i,d) avec i l'indice
    modifié et d la diminution qu'on lui applique.
    par exemple, si la position est [5,8,8,9], le coup (1,2) amène
    à la position [5,6,8,9]"""
    coups = []
    for i in range(0,len(position)):
        # On regarde les coups possibles diminuant l'indice [i]
        # on prend l'élément précédent dans la liste ou 0 si i = 0
        precedent = 0 if i == 0 else position[i-1]
        # et l'élément courant
        courant = position[i]
        # les diminutions possibles sont entre 1 et
        # courant - précédent (inclus)
        for d in range(1,courant - precedent + 1):
            coups.append((i,d))
    return(coups)

# Quelques remarques:
# - les couples en python, sont comme des listes
#   (1,2) est presque pareil que [1,2]
# Mais on ne peut pas modifier un couple.

l = [1,2] # mettez un couple, ça ne marchera plus!
l[1] = 5
l.append(3)

# - l.append permet d'ajouter un élément à la fin d'une liste.
# - python possible un if pour les "expressions" sur la ligne
#       precedent = 0 if i == 0 else position[i-1]

# Question 2: Explique la différence entre les deux if de python
# ...
# ...

# Question 3: teste la fonction coups_possibles, avec plusieurs
# exemples

# Question 4: complète la fonction suivante.
def joue(position,coup):
    """joue le coup indiqué à partir de la position donnée et renvoie
    la nouvelle position"""
    (i,d) = coup
    position = copy(position)
    position[i] = None # à modifier
    assert(position[i] >= 0)
    if i > 0:
        assert(position[i] >= position[i-1])
    return(position)

# Question 5: à quoi servent les deux lignes avec assert dans la
# fonction joue
# ....

# Question 6: à quoi sert copy?
# ....

# Question 7: la fonction suivante demande un coup à un joueur humain.
# modifie la pour qu'elle redemande un coup si la réponse du joueur
# est invalide.

def coups_humain(position,coups):
    """demande à un joueur humain de choisir un des coups possibles
    la position est utilisée pour un affichage sympathique.
    La fonction retourne la nouvelle position."""
    print(position)
    for i in range(0,len(coups)):
        print("coup", i, ":", coups[i], "=>", joue(position,coups[i]))
    i = int(input("votre coup : "))
    # ajoutez votre code ici
    coup = coups[i]
    position = joue(position,coup)
    return(position)

# Question 8: la fonction suivante joue une partie entre deux joueurs
# humain jusqu'à la fin. Complète la.
def joue_partie(position):
    """joue une partie complète avec deux joueurs humain"""
    coups = coups_possibles(position)
    while(coups != []):
        position = None # à modifier
        coups = None # à modifier
    print("vous avez perdu")

# on lance une partie ... à ne faire qu'après la question 8
# joue_partie([1,3,5,7])

# Question 9: modifie joue_partie et coup_humain pour afficher le nom
# du joueur qui doit jouer maintenant. On utilisera
# joue_partie([1,3,5,7],"Tamatoa","Simon") pour jouer une partie
# entre Simon et Tamatoa, si Tamatoa commence.
# aide: en python, on peut écrire (i,j) = (j,i) pour échanger
# la valeur de deux variables.

# Question 10: crée une fonction joue_aleatoire, qui choisit
# un coup au hasard. Cherche sur internet pour trouver comment
# choisir un élément au hasard dans une liste

# Question 11: modifie joue_partie pour qu'un humain puisse jouer
# contre l'ordinateur qui joue un coup au hasard. 

