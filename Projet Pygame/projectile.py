# Créé par meziane_a3, le 20/10/2022 en Python 3.7

import pygame

class Projectile:


    def __init__(self, position):
        self.position = position
        self.vitesse = 5
        self.degat = 10
        self.rect = pygame.Rect(self.position[0], self.position[1], 10, 30)
        self.active = False

    def isActive(self):
        return self.active

    def show(self, window):
        self.active = True
        pygame.draw.rect(window, (255,0,0), self.rect)

    def update(self, posXRocket):
        self.position[0] = posXRocket[0]
        self.position[1] += self.vitesse











