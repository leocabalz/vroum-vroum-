#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys, pygame
from pygame.locals import *

pygame.init()

#background = width, height = 1024, 748
TAILLE_ECRAN = LARGEUR, HAUTEUR = 1000, 800
TAILLE_CELLULE = 25
COULEUR = (155,155,155) # gris
EPAISSEUR = 5

screen = pygame.display.set_mode(TAILLE_ECRAN)
screen.fill((255,255,255))

#
# Fonction permettant de dessiner la grille du labyrinthe
#
def grille(screen, largeur, hauteur, taille_de_cellule):
    for x in range(0, largeur, taille_de_cellule):
        pygame.draw.line(screen, (0,0,0), (x,0), (x, hauteur))
    for y in range(0, hauteur, taille_de_cellule):
        pygame.draw.line(screen, (0,0,0), (0, y), (largeur, y))

#
# Fonction permettant de dessiner les murs des cellules 
# Il y a quatre murs E,O,N et S
#
def dessine_mur(screen, cellule, direction):
    pass

#
# Cellule objet qui contient les informations sur ses murs et autres
# Référence : http://ilay.org/yann/articles/maze/
# 
class Cellule(object):
    def __init__(self):
        # par défaut toutes les portes d'une cellule sont fermés
        self.mur_ouest = True
        self.mur_est = True
        self.mur_nord = True
        self.mur_sud = True
        # et la cellule n'a jamais été visitée
        self.deja_visite = False

    # TODO écrire les trois autres méthodes permettant d'abattre les murs
    def ouvrir_mur_ouest(self) :
        self.mur_ouest = False

    def ouvrir_mur_est(self) :
        self.mur_est = False

    def visite(self):
        self.deja_visite = True


#
# Un labyrinthe est un regroupement de Cellule
#
class Labyrinthe(object):

    #
    # initialisation du labyrinthe comme une liste de liste contenant des Cellules
    #
    def __init__(self, nb_ligne, nb_colonne):
        self.dedale = list() 
        for i in range(nb_ligne) :
            ligne = list()
            for j in range(nb_colonne):
                ligne.append(Cellule())
            self.dedale.append(ligne)


    # 
    # méthode d'affichage du labyrinthe sur l'écran
    # 
    def affichage(self, screen):
        i = 0
        j = 0
        for ligne in self.dedale :
            for cellule in ligne :
                # TODO
                # Compléter l'affichage des cellules
                if cellule.mur_ouest :
                    pygame.draw.rect(screen, COULEUR, (i*TAILLE_CELLULE, j*TAILLE_CELLULE, EPAISSEUR, TAILLE_CELLULE))
                if cellule.mur_est :
                    pygame.draw.rect(screen, COULEUR, ((i+1)*TAILLE_CELLULE, j*TAILLE_CELLULE, EPAISSEUR, TAILLE_CELLULE))    
                if cellule.mur_nord :
                    pygame.draw.rect(screen, COULEUR, (i*TAILLE_CELLULE, j*TAILLE_CELLULE, TAILLE_CELLULE, EPAISSEUR))
                if cellule.mur_sud :
                    #XXX
                    pass
                j = j+1
            j = 0
            i = i+1




horloge = pygame.time.Clock()
#boucle d'affichage


#
# TODO
# Déterminer la taille du labyrinthe à partir de la taille de l'écran et de la TAILLE_CELLULE
# 
lab = Labyrinthe(7,12)
print lab.dedale
print lab.dedale[1][4]


continuer = True
while continuer:

    horloge.tick(30)
   
#pour fermer la fenetre
    for event in pygame.event.get() :
        is_pressed = pygame.key.get_pressed()
        k_space = False
        if is_pressed[K_SPACE] :
            k_space = True
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE :

            continuer = False

    #affiche grille    
    grille(screen, 1000,800, TAILLE_CELLULE)

    # affiche labyrinthe
    lab.affichage(screen)



    pygame.display.flip()
