# Créé par moinootheen_z, le 11/10/2022 en Python 3.7
import pygame


pygame.init()

fenetre = pygame.display.set_mode((1080,720))
pygame.display.set_caption("Space Invaders")

image = pygame.image.load("title.png")
image = pygame.transform.scale(image, (540,360))

fenetre.blit(image, ((250, 50)))
pygame.display.update()

Launched = True

while Launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Launched = False


pygame.quit()
