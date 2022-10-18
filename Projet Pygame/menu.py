# Créé par moinootheen_z, le 11/10/2022 en Python 3.7
import pygame


pygame.init()

ecran = 0

fenetre = pygame.display.set_mode((1080,720))
pygame.display.set_caption("Space Invaders")

image = pygame.image.load("title.png")
image = pygame.transform.scale(image, (540,360))
image1 = pygame.image.load("start_bouton.png")
image1 = pygame.transform.scale(image1, (120, 30))

rect = image1.get_rect()
rect.x = 470
rect.y = 500

Launched = True

while Launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Launched = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()


            if rect.collidepoint(pos):
                ecran = 1






    if ecran == 0:
        fenetre.blit(image, ((250, 50)))
        fenetre.blit(image1, (rect))

    elif ecran == 1:
        fenetre.fill((255,255,0))

    pygame.display.flip()


pygame.quit()
