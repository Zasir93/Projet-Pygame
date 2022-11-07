
import pygame
import setting
import random

class Meteor:

    def __init__(self, health, image, range):
        self._health = health
        self._max_health = self._health
        self.images = image
        self.image = self.images[0]
        self.pos = pygame.Rect(300, -100, 100, 100)
        self.speed = 10
        self.show_able = True
        self.range = range

    def show(self, window):
        if self.show_able:
            window.blit(self.image, self.pos)
    
    def newMeteor(self):
        self.pos.y = -random.randint(setting.meteor_size[1], setting.meteor_size[1]+200)
        self.pos.x = random.randint(self.range[0], self.range[1]-self.pos.w)
        self._health = self._max_health
        self.show_able = True

    def update(self):
        if self.pos.y <= setting.window_size[1]+20:
            self.pos.y += self.speed
        else:
            self.newMeteor()

    def set_damage(self, damage_point):
        self._health -= damage_point
        if self._health < 0:
            self._health = 0
    
    def is_destroy(self):
        if self._health == 0:
            self.show_able = False

    def setMeteorsLevel(self, score):
        if score == 15:
            self.image = self.images[1]
            self._max_health = 2
        
        if score == 35:
            self.image == self.images[2]
            self._max_health = 3
            self.speed = 15