
import pygame
import setting
import lazer

class Player():
    """
        Classe player qui gère le joueur et ses actions
        _name: nom du joueur
        _health: vie du joueur
        _max_health: vie max
        _damage_point: dégât
        _image: image du vaisseau
        _speed: vitesse
        _shield: nombre de bouclier
        _shield_rect: position bouclier
        _shield_showable: montrer le bouclier ou pas
        score: score du joueur
        _health_Points_Image: image des points de vie
        pos_health_points: position de l'image des points de vie
        _pos: position joueur
        lazers: liste des munitions lazer du joueur 
    """
    def __init__(self, name, health, damage, image, health_image, lazer_image):
        self._name = name
        self._health = health
        self._max_health = self._health
        self._damage_point = damage
        self._image = image
        self._speed = 10
        self._shield = 3
        self._shield_rect = pygame.Rect(0,0,0,0)
        self._shield_showable = False

        self.score = 0

        self._health_Points_Image = health_image
        self.pos_health_points = pygame.Rect(20, 15, 200, 134)

        self._pos = pygame.Rect(500, 720-150, 100, 100)

        self.lazers = []

        for i in range(2):
            self.lazers.append(lazer.Lazer(self._pos.x+(self._pos.y/2), self._pos.y, lazer_image, self._damage_point))

    def __str__(self):
        return (f"Nom : {self._name} \nPoint de vie : {self._health} \nPoint d'attaque : {self._damage_point}")


    def showHealthPoint(self, window):
        """
            affiche les points de vie
        """
        window.blit(self._health_Points_Image[self._health], self.pos_health_points)

    def show(self, window):
        """
        affiche le joueur
        """
        #pygame.draw.rect(window, (255,0,0), self._pos, 1)
        window.blit(self._image, self._pos)

    def move(self, direction):
        """
            gestion deplacement
        """
        vX = 0
        vY = 0
        if direction == 'u':
            vY = -1
        elif direction == 'd':
            vY = 1
        elif direction == 'r':
            vX = 1
        elif direction == 'l':
            vX = -1

        if self._pos.x + (vX*self._speed) >= 0 and self._pos.x + (vX*self._speed)+100 <= setting.window_size[0]:
            if (self._pos.y + (vY*self._speed) >= 0 and self._pos.y + (vY*self._speed)+100 <= setting.window_size[1]):
                self._pos.x += (vX*self._speed)
                self._pos.y += (vY*self._speed)

    def collision(self, meteor):
        """
            gestion collision avec météor
        """
        if meteor.show_able:
            return self._pos.colliderect(meteor.pos)
        return False

    def collisionBullet(self, meteor):
        """"
            gestion collision du lazer avec météor
        """
        for lazer in self.lazers:
            if lazer.collision(meteor):
                lazer.show_able = False
                return True
        return False

    def is_dead(self):
        """
            gestion de la vie du joueur
        """
        return self._health <= 0

    def shoot(self):
        """
            tire un lazer
        """
        for lazer in self.lazers:
            if lazer.show_able == False:
                lazer.show_able = True
                lazer.pos.x = self._pos.x
                lazer.pos.y = self._pos.y
                break

    def showLazers(self, window):
        """
            affiche les lazers
        """
        for lazer in self.lazers:
            if lazer.show_able == True:
                lazer.show(window)

    def updateLazers(self):
        """
            mise à jour lazer
        """
        for lazer in self.lazers:
            if lazer.show_able == True:
                lazer.update(self._pos)

    def changeSpaceshipSkin(self, newOneImage):
        """
            change de skin à partir du magazin
        """
        newOneImage = pygame.transform.scale(newOneImage, (100,100))
        self._image = newOneImage

    def showShield(self, window):
        """
            affiche le bouclier
        """
        if self._shield_showable and self._shield > 0:
            self._shield_rect.x = self._pos.x - 40
            self._shield_rect.y = self._pos.y - 40
            self._shield_rect.w = 180
            self._shield_rect.h = 180

            center = (self._pos.x+50, self._pos.y+50)
            pygame.draw.circle(window, (0,255,255), center, self._pos.w, 3)
            #pygame.draw.rect(window, "white", self._shield_rect, 2)

    def collisionShield(self, meteor):
        """
            gestion collision météor avec bouclier
        """
        if self._shield_showable and meteor.show_able:
            if self._shield_rect.colliderect(meteor.pos):
                return True
        return False

    def stillShield(self):
        """
            gestion de vie du bouclier
        """
        if self._shield <= 0:
            self._shield_showable = False

