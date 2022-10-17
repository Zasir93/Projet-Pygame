# Créé par moinootheen_z, le 11/10/2022 en Python 3.7
import pygame


pygame.init()

fenetre = pygame.display.set_mode((1080,720))
pygame.display.set_caption("Space Invaders")

image = pygame.image.load("title.png")
image = pygame.transform.scale(image, (540,360))
image1 = pygame.image.load("start_bouton.png")




Launched = True

while Launched:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN :
            print("Zasir le bg")
        if event.type == pygame.QUIT:
            Launched = False
    fenetre.blit(image, ((250, 50)))
    fenetre.blit(image1, ((340, 500)))
    pygame.display.update()


pygame.quit()
