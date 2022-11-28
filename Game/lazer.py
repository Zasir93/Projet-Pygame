
import pygame

class Lazer:
    """
    Classe qui gère les tirs du vaisseau
    pos: position du lazer
    image: image du lazer
    show_able: si le lazer est à montré ou pas
    speed: vitesse du lazer
    damage: dégat du lazer
    """
    def __init__(self,  posX, posY, image, dmg):
        self.pos = pygame.Rect(posX, posY, 40, 10)
        self.image = image
        self.show_able = False
        self.speed = 30
        self.damage = dmg

    def show(self, window):
        """
        affichage du lazer
        """
        if self.show_able:
            window.blit(self.image, self.pos)

    def update(self, pos_spaceship):
        """
        mise à jour de la position
        """
        if self.show_able:
            self.pos.y -= self.speed

        if self.pos.y <= 0:
            self.show_able = False
            self.pos.x = pos_spaceship.x+(self.pos.w / 2)
            self.pos.y = pos_spaceship.y
    
    def collision(self, meteor):
        """
        détéction des collision avec un météor
        """
        if meteor.show_able and self.show_able:
            return self.pos.colliderect(meteor.pos)
        return False