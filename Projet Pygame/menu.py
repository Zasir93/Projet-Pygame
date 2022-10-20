# Créé par moinootheen_z, le 11/10/2022 en Python 3.7
import pygame
import player
import projectile

pygame.init()

ecran = 0

fenetre = pygame.display.set_mode((1080,720))
pygame.display.set_caption("Space Invaders")

image = pygame.image.load("title.png")
image = pygame.transform.scale(image, (540,360))
image1 = pygame.image.load("start_bouton.png")
image1 = pygame.transform.scale(image1, (120, 30))

imagePlayer = pygame.image.load("rocket.jpg")
imagePlayer = pygame.transform.scale(imagePlayer, (100,100))
player1 = player.Player("Zasir", 1, 100, 3, imagePlayer)

rect = image1.get_rect()
rect.x = 470
rect.y = 500

Launched = True

pygame.key.set_repeat(100)



while Launched:
    keys = pygame.key.get_pressed()
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
        if keys[pygame.K_RIGHT]:
            player1.moveX(3)
        if keys[pygame.K_LEFT]:
            player1.moveX(-3)

        if keys[pygame.K_SPACE]:
            player1.bullet.show(fenetre);


        if player1.bullet.isActive():
            player1.bullet.update(player1.getPosition())

        player1.show(fenetre)



    pygame.display.flip()


pygame.quit()
