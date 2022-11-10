
import pygame

class Menu:
    def __init__(self, imageBG, imageStart):
        self.imageBG = imageBG
        self.imageStart = imageStart

    def showBackground(self, window):
        window.blit(self.imageBG, (0,0))

    def showStartButton(self, window):
        window.blit(self.imageStart, (200,200))

pygame.init()
window = pygame.display.set_mode((1080, 720))


imageStartButton = pygame.image.load("GAME/MENU/start.png")
imageBGMenu = pygame.image.load("GAME/MENU/bg.png")
menu = Menu(imageBGMenu, imageStartButton)

menu.showBackground(window)
menu.showStartButton(window)
pygame.display.flip()

start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

pygame.quit()