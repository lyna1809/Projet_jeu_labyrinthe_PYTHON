# PREMIERE PARTIE
# TRAVAIL PREPARATOIRE:
# import sys
import turtle


def labyFromFile(fn):
    """
    Lecture d'un labyrinthe dans le fichier de nom fn
    Read a maze from the file named fn.
    """
    f = open(fn)
    laby = []
    indline = 0
    for fileline in f:
        labyline = []
        inditem = 0
        for item in fileline:
            # empty cell / case vide
            if item == ".":
                labyline.append(0)
            # wall / mur
            elif item == "#":
                labyline.append(1)
            # entrance / entree
            elif item == "x":
                labyline.append(0)
                mazeIn = [indline, inditem]
            # exit / sortie
            elif item == "X":
                labyline.append(0)
                mazeOut = [indline, inditem]
            # discard "\n" char at the end of each line
            inditem += 1
        laby.append(labyline)
        indline += 1
    f.close()
    return laby, mazeIn, mazeOut


# ====Test laby0 ou bien laby1: =========================================================================
# importer le fichier:
fn = "laby1.laby"
(laby, mazeIn, mazeOut) = labyFromFile(fn)
x0 = 0
y0 = 0
taille_cell = 20
dicofig = {"x0": x0, "y0": y0, "taille_de_la_cellule": taille_cell}
# cree un dictionnaire dicojeu qui prend tout les cordonnés onligatoire:
dicojeu = {"a": laby, "b": mazeIn, "c": mazeOut, "config": dicofig}


# =============================================================================

def afficheTextuel(dicojeu):
    i = 0
    while i < len(laby):
        j = 0
        while j < len(laby[0]):
            # un mur:
            if laby[i][j] == 1:
                print("#", end="")
            if laby[i][j] == 0:
                # une sortie:
                if i == dicojeu[0][0] and j == dicojeu[0][1]:
                    print("x", end="")
                # une entree:
                if i == dicojeu[1][0] and j == dicojeu[1][1]:
                    print("o", end="")
                # un espace de mouvement:
                else:
                    print(" ", end="")
            j += 1
        print("\n")
        i += 1


# une fonction carree pour tarcer avec les murs:
def carre(taille_cell):
    # trace un carre de taille 20
    i = 1  # compteur du nb de cotes
    while i <= 4:
        turtle.forward(taille_cell)
        turtle.right(90)
        i = i + 1

    # le tracer du labyrinthe:


def affichegraphique(dicojeu, taille_cell):
    turtle.up()
    turtle.goto(0, 0)
    for i in range(len(laby)):
        for j in range(len(laby[i])):
            # mur:
            if laby[i][j] == 1:
                turtle.down()
                # turtle.begin_fill() nous permet de colorer l'interieur du carree:
                turtle.begin_fill()
                carre(taille_cell)
                turtle.end_fill()
                turtle.forward(taille_cell)
            elif laby[i][j] == 0 and j == len(laby[i]) - 1:
                turtle.down()
                turtle.color("green")
                turtle.begin_fill()
                carre(taille_cell)
                turtle.end_fill()
                turtle.forward(taille_cell)
            elif laby[i][j] == 0 and j != len(laby[i]) - 1 and j != 0:
                turtle.up()
                turtle.forward(taille_cell)
            elif laby[i][0] == 0:
                turtle.down()
                turtle.color("green")
                turtle.begin_fill()
                carre(taille_cell)
                turtle.end_fill()
                turtle.forward(taille_cell)
            turtle.color("black")
        turtle.up()
        turtle.goto(0, 0 - (i + 1) * taille_cell)


# turtle.speed(100)
# affichegraphique(dicojeu,20)

# METHODE01:
# convertir les pixels en cell:
def pixel2cell(xp, yp, x0, y0, taille_cell):
    # j est le nombre de colonnes:
    j = int((xp - x0) // taille_cell)
    # i est le nombre de lignes:
    i = int(((y0 - yp) // taille_cell))
    return i, j


# print(pixel2cell(20,0,0,0,20))

# METHODE02:
# def pixel2cell(x,y):
#     taille_cellule=dicojeu['config']['taille_de_la_cellule']
#     x0=dicojeu['config']['x0']
#     y0=dicojeu['config']['y0']
#     colonne = -1
#     ligne = -1
#     while x-x0>=0:
#         x=x-taille_cellule
#         colonne=colonne+1
#     while y-y0<=0:
#         y=y+taille_cellule
#         ligne=ligne+1
#     return [ligne,colonne]
# print(pixel2cell(0,-20))


def testClic(xp, yp):
    global laby
    x0 = 0
    y0 = 0
    taille_cell = 20
    # appel a la fonction de pixel2cell pour recuperer le numero de ligne et colonnes:
    m = pixel2cell(xp, yp, x0, y0, taille_cell)
    i = m[0]  # i est le nombre de lignes
    j = m[1]  # j est le nombre de colonnes
    # si le clic est a l'interieur du labyrinthe:
    if i >= 0 and j >= 0 and i <= len(laby) and j < len(laby[0]):
        # si clic est a l'interieur du laby:
        print("Le numero de lignes est: ", i)
        print("Le numero de colonnes est: ", j)
    else:
        # si le clic est hors du laby:
        print("Error")
    # print(testClic(20,0))


# turtle.speed(100)
# affichegraphique(dicojeu,taille_cell)
# turtle.onscreenclick(testClic)
# turtle.mainloop()

# METHODE01:
# convertir des cell en pixel:
def cell2pixel(i, j, x0, y0, taille_cell):
    x0 = x0 + taille_cell / 2
    y0 = y0 - taille_cell / 2
    xp = (i * taille_cell + x0)
    yp = (-j * taille_cell + y0)
    return xp, yp


# print(cell2pixel(0,10,0,0,20))

# METHODE02:
# def cell2pixel(i,j):
#     x=dicojeu['config']['x0']+dicojeu['config']['taille_de_la_cellule']/2
#     y=dicojeu['config']['y0']-dicojeu['config']['taille_de_la_cellule']/2
#     while i>0:
#         x=x+dicojeu['config']['taille_de_la_cellule']
#         i=i-1
#     while j>0:
#         y=y-dicojeu['config']['taille_de_la_cellule']
#         j=j-1
#     return [x,y]
# print(cell2pixel(0,10))


# methode01:
def typeCellule(i, j, taille_cell, dicojeu):
    # entree:
    if [i, j] == dicojeu["b"]:
        return "entree"
    # sortie:
    elif [i, j] == dicojeu["c"]:
        return "sortie"
        # un passage mais qui n'est ni un entrée ni une sortie:
    elif laby[i][j] == 0 and laby[i][j] != dicojeu["b"] and laby[i][j] != dicojeu["c"]:
        return "passage"
    # un mur:
    elif laby[i][j] == 1 and i < len(laby) and j < len(laby[i]):
        return "mur"
    # print(typeCellule(11,0,20,dicojeu))


def typeCellule_modifie(i, j, dicojeu, taille_cell):
    p = 0
    # entree:
    if [i, j] == dicojeu["b"]:
        return "entree"
    elif [i, j] == dicojeu["c"]:
        return "sortie"
    # passage modifié:
    # if(i,j) est un passage:
    elif laby[i][j] == 0 and laby[i][j] != dicojeu["b"] and laby[i][j] != dicojeu["c"]:
        # verifier pour toutes les cases voisines pour voir dans quel cas on se trouve:
        if laby[i][j + 1] == 0:  # si la case de droite est un espace:
            p += 1  # on incremente le compteur "p"
        if laby[i][j - 1] == 0:  # de meme de toutes les autres cases:
            p += 1
        if laby[i + 1][j] == 0:
            p += 1
        if laby[i - 1][j] == 0:
            p += 1
        if p == 1:
            return "impasse"
        elif p >= 3:
            return "careffour"
        else:
            return "standard"
    else:
        return "mur"
    # print(typeCellule_modifie(9,14,dicojeu,20))


# methode02:

# définition de la fonction compte_mur qui compte le nombre de mur autour d'une case (elle reçoit en argument la colonne et la ligne de cette case)
# NB cette fonction n'est valable que pour les cases vides (les passages)

# def compte_mur(ligne,colonne):
#     laby=dicojeu['a']
#     i=0
#     if laby[ligne+1][colonne]==1: #un mûr au dessus
#         i=i+1
#     if laby[ligne-1][colonne]==1: #un mûr au dessous
#         i=i+1
#     if laby[ligne][colonne+1]==1: #un mûr à droite
#         i=i+1
#     if laby[ligne][colonne-1]==1: #un mûr à gauche
#         i=i+1
#     return i

# def typeCellule(ligne,colonne):
#     laby=dicojeu['a']
#     #nombre de colonnes total:
#     n_col=len(laby[0])
#     #nombre de lignes total:
#     n_lig=len(laby)
#     #correspondance:
#     ch=""
#     if colonne == 0 and laby[ligne][0]==0:
#         ch="entrée"
#     elif colonne ==(n_col-1) and laby[ligne][n_col-1]==0:
#         ch="sortie"
#     elif laby[ligne][colonne] == 0 and colonne != len(laby[ligne])-1 and colonne!=0:
#         #dans le cas où la case est un passage:
#         if compte_mur(ligne,colonne) == 1:
#             ch="carrefour"
#         elif compte_mur(ligne,colonne) == 2:
#             ch="passage standard"
#         elif compte_mur(ligne,colonne) == 3:
#             ch="impasse"
#     else :
#         ch="mur"
#     return ch
# print(typeCellule(ligne,colonne))


# partie2:
# definir la liste des commandes du joueur (liste_vide):
liste_commandes = []


def gauche():
    # xi et yi sont utiliser pour recuperer les copordonnee actuelle de la tortue:
    xi = turtle.xcor()
    yi = turtle.ycor()
    turtle.up()
    turtle.left(180)
    turtle.forward(20)
    turtle.left(180)
    taille_cell = 20
    verif(xi, yi, taille_cell, dicojeu)
    print("gauche ; left")
    # si le joueur part a gauche, "G" se rajoute a la listes des commandes:
    print(liste_commandes.append("G"))


def droite():
    xi = turtle.xcor()
    yi = turtle.ycor()
    turtle.up()
    turtle.forward(20)
    taille_cell = 20
    verif(xi, yi, taille_cell, dicojeu)
    print("droite ; right")
    # si le joueur part a droite, "D" se rajoute a la listes des commandes:
    print(liste_commandes.append("D"))


def bas():
    xi = turtle.xcor()
    yi = turtle.ycor()
    turtle.up()
    turtle.right(90)
    turtle.forward(20)
    turtle.right(270)
    taille_cell = 20
    verif(xi, yi, taille_cell, dicojeu)
    print("bas ; down")
    # si le joueur part en bas, "B" se rajoute a la listes des commandes:
    print(liste_commandes.append("B"))


def haut():
    xi = turtle.xcor()
    yi = turtle.ycor()
    turtle.up()
    turtle.left(90)
    turtle.forward(20)
    turtle.left(270)
    taille_cell = 20
    verif(xi, yi, taille_cell, dicojeu)
    # si le joueur part au haut, "H" se rajoute a la listes des commandes:
    print(liste_commandes.append("H"))
    print("haut ; up")


# #faire marcher la tortue sur les passages:
def verif(xi, yi, taille_cell, dicojeu):
    # recuperer les codonnes de la totue en pixel:
    xp = turtle.xcor()
    yp = turtle.ycor()
    # convertir les coordonnes en cell:
    [i, j] = pixel2cell(xp, yp, 0, 0, taille_cell)
    # remmettre la couleurs original a la tortue:
    turtle.fillcolor("black")
    m = testClic(xp, yp)
    if m != "Error":  # si le clic n'est pas a l'extieur du laby:
        [i, j] = pixel2cell(xp, yp, 0, 0, taille_cell)
        # verifier le type de cette cellule:
        s = typeCellule_modifie(i, j, dicojeu, 20)
        if s == "mur":
            turtle.fillcolor("red")  # la couleure du curseur en rouge
            turtle.goto(xi, yi)  # la bloquer
        if s == "impasse":  # remttre la couleure jaune pour une impasse:
            turtle.fillcolor("yellow")
        if s == "careffour":  # remttere la couleure bleue pour un carffour:
            turtle.fillcolor("blue")
        if s == "sortie":  # sur la case de sortie changer laa couleure en vert et afficher un message de victoire:
            turtle.fillcolor("green")
            print("Victoire!")

        # key bindings


turtle.onkeypress(gauche, "Left")
turtle.onkeypress(droite, "Right")
turtle.onkeypress(haut, "Up")
turtle.onkeypress(bas, "Down")
turtle.listen()

# start loop
turtle.speed(100)
turtle.goto(0,0)

affichegraphique(dicojeu,taille_cell)
# diriger la tortue a l'entree:
(jentre,ientre)= dicojeu["b"]
(xentre,yentre)=cell2pixel(ientre,jentre,0,0,20)
turtle.up()
# plus exactement au centre de la cellule:
turtle.goto(xentre,yentre)
turtle.down()
xi=turtle.xcor()
yi=turtle.ycor()
verif(xi,yi,20,dicojeu)
turtle.mainloop()

#methode01:
def explorer():
    chemin_parcouru_i=[]
    chemin_parcouru_j=[]
    chemin_carrefour=[]
    [i,j]= dicojeu["b"]
    (xentre,yentre)=cell2pixel(j,i,0,0,20)
    turtle.up()
    # plus exactement au centre de la cellule:
    turtle.goto(xentre,yentre)
    turtle.down()
    chemin_parcouru_i.append(i)
    chemin_parcouru_j.append(j)
    while laby[i][j] != dicojeu["c"]:
        # standard:
            if (typeCellule_modifie(i, j, dicojeu, 20)=="standard" or typeCellule_modifie(i, j, dicojeu , 20)=="entree") and typeCellule_modifie(i, j, dicojeu , 20)!="mur":

                    if typeCellule(i, j+1 ,20, dicojeu)=="passage" and (j+1 not in chemin_parcouru_j and i in chemin_parcouru_i) :

                        turtle.up()
                        turtle.forward(20)
                        j+=1
                        chemin_parcouru_i.append(i)
                        chemin_parcouru_j.append(j)
                        turtle.down()
                    elif typeCellule(i-1, j ,20, dicojeu)=="passage"  :
                        turtle.up()
                        turtle.left(90)
                        turtle.forward(20)
                        turtle.left(270)
                        turtle.down()
                        i-=1
                        chemin_parcouru_i.append(i)
                        chemin_parcouru_j.append(j)
                    elif typeCellule(i, j-1 ,20, dicojeu)=="passage" :

                        turtle.up()
                        turtle.left(180)
                        turtle.forward(20)
                        turtle.left(180)
                        turtle.down()
                        j-=1
                        chemin_parcouru_i.append(i)
                        chemin_parcouru_j.append(j)


                    elif typeCellule(i+1, j ,20, dicojeu)=="passage" and (i+1 not in chemin_parcouru_i):
                      turtle.up()
                      turtle.right(90)
                      turtle.forward(20)
                      turtle.right(270)
                      turtle.down()
                      i=i+1
                      chemin_parcouru_i.append(i)
                      chemin_parcouru_j.append(j)


            elif typeCellule_modifie(i, j, dicojeu, 20)=="careffour":
                    if typeCellule(i-1, j ,20, dicojeu)=="passage" :
                        turtle.up()
                        turtle.left(90)
                        turtle.forward(20)
                        turtle.left(270)
                        turtle.down()
                        i=i-1
                        couple2=(i-1,j)
                        chemin_carrefour.append(couple2)

                    elif typeCellule(i, j-1 ,20, dicojeu)=="passage" :

                        turtle.up()
                        turtle.left(180)
                        turtle.forward(20)
                        turtle.left(180)
                        turtle.down()
                        j=j-1
                        couple4=(i,j-1)
                        chemin_carrefour.append(couple4)
                    elif typeCellule(i, j+1 ,20, dicojeu)=="passage" :

                      turtle.up()
                      turtle.forward(20)
                      j=j+1
                      couple3= (i,j+1)
                      chemin_carrefour.append(couple3)
                      turtle.down()

                    elif typeCellule(i+1, j ,20, dicojeu)=="passage" :
                      turtle.up()
                      turtle.right(90)
                      turtle.forward(20)
                      turtle.right(270)
                      turtle.down()
                      i=i+1
                      Couple1=(i+1,j)
                      chemin_carrefour.append(Couple1)


turtle.speed(100)
affichegraphique(dicojeu, taille_cell)
a=explorer()


"""
# methode02:
def right(i, j):
    if laby[i][j + 1] != 1:
        j += 1
        turtle.up()
        turtle.forward(20)

        return i, j, "droite"

    else:

        return "pas possible"


def left(i, j):
    if laby[i][j - 1] != 1:
        j -= 1
        turtle.up()
        turtle.left(180)
        turtle.forward(20)
        turtle.left(180)
    return i, j, "gauche"


def up(i, j):
    if laby[i - 1][j] != 1:
        i -= 1
        turtle.up()
        turtle.left(90)
        turtle.forward(20)
        turtle.left(270)
        return i, j, "haut"

    else:

        return "pas possible"


def down(i, j):
    if laby[i + 1][j] != 1:
        i += 1
        turtle.up()
        turtle.right(90)
        turtle.forward(20)
        turtle.right(270)

    return i, j, "bas"


def recherche_index(chemin):
    indice_car = []
    index = 0
    for index in range(len(chemin)):
        if chemin[index] == "carrefour":
            indice_car.append(index)
    index_max = max(indice_car)

    return index_max


def explorer():
    (i, j) = dicojeu["b"]
    chemin = []
    d = right(i, j)
    i = d[0]
    j = d[1]
    genre = typeCellule_modifie(i, j, dicojeu, taille_cell)
    chemin.append((d, genre))

    while [i, j] != dicojeu["c"]:

        if genre != "impasse" and genre != "sortie":

            if d[2] == "droite":
                d = up(i, j)
                if d == "pas possible":
                    d = right(i, j)
                    if d == "pas possible":
                        d = down(i, j)


            elif d[2] == "haut":
                d = right(i, j)
                if d == "pas possible":
                    d = up(i, j)
                    if d == "pas possible":
                        d = left(i, j)

            elif d[2] == "gauche":
                d = up(i, j)
                if d == "pas possible":
                    d = left(i, j)
                    if d == "pas possible":
                        d = down(i, j)
            elif d[2] == "bas":
                d = right(i, j)
                if d == "pas possible":
                    d = down(i, j)
                    if d == "pas possible":
                        d = left(i, j)

        if genre == "impasse":
            index_carreffour = recherche_index(chemin)
            direction = chemin[index_carreffour][0][2]
            if direction == "droite":
                d = left(i, j)
                if d == "pas possible":
                    d = up(i, j)
                    if d == "pas possible":
                        d = down(i, j)
            if direction == "gauche":
                d = right(i, j)
                if d == "pas possible":
                    d = up(i, j)
                    if d == "pas possible":
                        d = down(i, j)
            if direction == "haut":
                d = right(i, j)
                if d == "pas possible":
                    d = left(i, j)
                    if d == "pas possible":
                        d = down(i, j)

            if direction == "bas":
                d = right(i, j)
                if d == "pas possible":
                    d = left(i, j)
                    if d == "pas possible":
                        d = up(i, j)

        i = d[0]
        j = d[1]
        genre = typeCellule_modifie(i, j, dicojeu, taille_cell)
        chemin.append((d, genre))
    chemin_new = []
    for i in range(len(chemin)):
        chemin_new.append(chemin[i][0][2])

    return chemin_new


# diriger la tortue a l'entree:
turtle.speed(100)
affichegraphique(dicojeu, 20)

(ientre, jentre) = dicojeu["b"]
(xentre, yentre) = cell2pixel(jentre, ientre, 0, 0, 20)
turtle.up()
# plus exactement au centre de la cellule:
turtle.goto(xentre, yentre)
turtle.down()
a = explorer()
"""

















