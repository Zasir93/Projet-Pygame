
import pygame
import setting

class BG:

    def __init__(self, image):
        self.image1 = image
        self.image2 = image
        self.speed = 15

        self.pos1 = self.image1.get_rect()
        self.pos2 = self.image2.get_rect()
        self.pos2.y = self.pos1.y - self.pos1.h

        self.font = pygame.font.SysFont("Arial", 50, False, False)

        self.timer = (0,0,0,0)

    def show(self, window):
        window.blit(self.image1, self.pos1)
        window.blit(self.image2, self.pos2)
    
    def update(self):
        self.pos1.y += 15 
        self.pos2.y += 15

        if self.pos1.y >= setting.window_size[1]:
            self.pos1.y = self.pos2.y - self.pos1.h
        if self.pos2.y >= setting.window_size[1]:
            self.pos2.y = self.pos1.y - self.pos1.h
    

    def showScore(self, score, window):
        textScore = self.font.render(f"{score}", False, (255,255,255))
        window.blit(textScore, setting.scorePos)

