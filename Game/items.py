
import pygame
import random

class Items:
    
    def __init__(self, image):
        self.image = image
        self.imageRect = self.image.get_rect()

        self.show_able = False
    
    def setPosition(self):
        self.imageRect.x = random.randint(10, 1000)
        self.imageRect.y = random.randint(100, 650)

    def show(self, window):
        if self.show_able:
            window.blit(self.image, self.imageRect)
    
    def collision(self, spaceship):
        if self.show_able:
            return self.imageRect.collidepoint(spaceship._pos)
        return False

class ItemsLive(Items):
    def __init__(self, image):
        super(image)
    
    def action(self, spaceship):
        if spaceship._hearth < spaceship._max_hearth:
            spaceship._hearth += 1
        return spaceship

class ItemsShield(Items):
    def __init__(self, image):
        super(image)
    
    def action(self, spaceship):
        spaceship._shield = random.randint(1,3)
        return spaceship
            