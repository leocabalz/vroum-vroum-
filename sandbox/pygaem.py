#!/usr/bin/python2

import sys, pygame
from pygame.locals import *

pygame.init()



#background = width, height = 1024, 748
size = width, height = 1000, 800
TAILLE_CELLULE = 25


screen = pygame.display.set_mode(size)
flulu = screen.fill((255,255,255))

def grille(screen, largeur, hauteur, taille_de_cellule):
    for x in range(0, largeur, taille_de_cellule):
        pygame.draw.line(screen, (0,0,0), (x,0), (x, hauteur))
    for y in range(0, hauteur, taille_de_cellule):
        pygame.draw.line(screen, (0,0,0), (0, y), (largeur, y))

horloge = pygame.time.Clock()
#boucle d'affichage

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
    
    #screen.fill((255,255,255))

    grille(screen, 1000,800, TAILLE_CELLULE)

    couleur = (155,155,155) # gris
    pygame.draw.rect(screen, couleur, (0,0,TAILLE_CELLULE,3))


    pygame.display.flip()
    
      
