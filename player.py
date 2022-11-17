
import pygame
import setting
import lazer

class Player():

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
        window.blit(self._health_Points_Image[self._health], self.pos_health_points)

    def show(self, window):
        #pygame.draw.rect(window, (255,0,0), self._pos, 1)
        window.blit(self._image, self._pos)

    def move(self, direction):
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
        if meteor.show_able:
            return self._pos.colliderect(meteor.pos)
        return False

    def collisionBullet(self, meteor):
        for lazer in self.lazers:
            if lazer.collision(meteor):
                lazer.show_able = False
                return True
        return False

    def is_dead(self):
        return self._health <= 0

    def shoot(self, sound):
        sound.shootSound()
        for lazer in self.lazers:
            if lazer.show_able == False:
                lazer.show_able = True
                lazer.pos.x = self._pos.x
                lazer.pos.y = self._pos.y
                break

    def showLazers(self, window):
        for lazer in self.lazers:
            if lazer.show_able == True:
                lazer.show(window)

    def updateLazers(self):
        for lazer in self.lazers:
            if lazer.show_able == True:
                lazer.update(self._pos)

    def changeSpaceshipSkin(self, newOneImage):
        newOneImage = pygame.transform.scale(newOneImage, (100,100))
        self._image = newOneImage

    def showShield(self, window):
        if self._shield_showable and self._shield > 0:
            self._shield_rect.x = self._pos.x - 40
            self._shield_rect.y = self._pos.y - 40
            self._shield_rect.w = 180
            self._shield_rect.h = 180

            center = (self._pos.x+50, self._pos.y+50)
            pygame.draw.circle(window, (0,255,255), center, self._pos.w, 3)
            #pygame.draw.rect(window, "white", self._shield_rect, 2)

    def collisionShield(self, meteor):
        if self._shield_showable and meteor.show_able:
            if self._shield_rect.colliderect(meteor.pos):
                return True
        return False

    def stillShield(self):
        if self._shield <= 0:
            self._shield_showable = False

