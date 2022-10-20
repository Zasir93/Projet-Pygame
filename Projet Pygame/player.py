
import pygame
import projectile



class Player:


    def __init__(self, name, niveau, pv, bouclier, image):
        self.name = name
        self.level = niveau
        self.health = pv
        self.health_max = pv
        self.shield = bouclier
        self.image = image
        self.pos = (200, 600)
        self.rectImage = pygame.Rect(self.pos[0], self.pos[1], 100, 100)
        self.bullet = projectile.Projectile(self.pos)

    def show(self, window):
        window.blit(self.image, self.rectImage)

    def moveX(self, vX):
        if (self.rectImage.x+self.rectImage.w + vX <= 1080 and self.rectImage.x + vX >= 0):
            self.rectImage.x += vX
            print(self.rectImage)

    def moveY(self, vY):
        self.rectImage.y += vY

    def getPosition(self):
        return (self.rectImage.x, self.rectImage.y)