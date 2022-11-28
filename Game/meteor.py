
import pygame
import setting
import random

class Meteor:
    """
    Classe qui gère les météorites
    _health: vie
    _max_health: vie max
    image: image du météor
    pos: position du météor
    speed: vitesse du météor
    show_able: si le météor est à affiché ou pas
    range: intervalle pour la position
    """
    def __init__(self, health, image, range):
        self._health = health
        self._max_health = self._health
        self.image = image
        self.pos = pygame.Rect(300, -100, 100, 100)
        self.speed = 10
        self.show_able = True
        self.range = range

    def show(self, window):
        """
            affichage du météor
        """
        if self.show_able:
            window.blit(self.image, self.pos)
    
    def newMeteor(self):
        """
            création d'un nouveau météor
        """
        self.pos.y = -random.randint(setting.meteor_size[1], setting.meteor_size[1]+200)
        self.pos.x = random.randint(self.range[0], self.range[1]-self.pos.w)
        self._health = self._max_health
        self.show_able = True

    def update(self):
        """
            mise à jour de la position
        """
        if self.pos.y <= setting.window_size[1]+20:
            self.pos.y += self.speed
        else:
            self.newMeteor()

    def set_damage(self, damage_point):
        """
            ajouter des dégâts
        """
        self._health -= damage_point
        if self._health < 0:
            self._health = 0
    
    def is_destroy(self):
        """
            vérifié si le météor est détruit
        """
        if self._health == 0:
            self.show_able = False
    
    def levelUp(self, score, time):
        """
            augmente la vie du météor soit en fonction du temps, soit du score
        """
        if score == 10 or time == 10:  
            self._max_health = 2
        if score == 30 or time == 30:
            self._max_health = 3
            self.speed = 12
        if score == 50 or time == 60:
            self.speed = 14