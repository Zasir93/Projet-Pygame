# Créé par monteiro_soar_g, le 20/10/2022 en Python 3.7
import pygame
import random

class Projectile:


    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.vitesse = 5
        self.degat = 10

    def deplacement(self):
        (x, y) = self.position
        delta_x = 5
        delta_y = random.randint(- 5, 5)
        self.position = (x + delta_x, y + delta_y)

    def affichage(self, surface):
        self.deplacement()
        surface.blit(self.image, self.position)
