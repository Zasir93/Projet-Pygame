
import pygame

pygame.init()

# window
window_size = (1080, 720)
window_title = "Shooter"

# position du score
scorePos = (980, 10)

# lié au jeu
spaceship_size = (100, 100)
meteor_size = (150,150)

# lié à l'écran
fps = 60
screen = 0



# image des composants du jeu ===========================================================================

menuBackgroundImage = pygame.image.load("MENU/bg.png")
menuBackgroundImage = pygame.transform.scale(menuBackgroundImage, (1080, 720))

buttonsImage = pygame.image.load("MENU/buttons.png")
playButtonImage = buttonsImage.subsurface(pygame.Rect(150, 35, 210, 90))
shopButtonImage = buttonsImage.subsurface(pygame.Rect(150, 145, 210, 90))

backgroundImage = pygame.image.load("GAME/space.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, window_size)

imageMoves = pygame.image.load("MENU/move.png")
imageSpace = pygame.image.load("MENU/space.png")
imageSpace = pygame.transform.scale(imageSpace, (300, 99))

imageTitle = pygame.image.load("MENU/title.png")


crossShopButtonImage = pygame.image.load("MENU/SHOP/cross.png")
crossShopButtonImage = pygame.transform.scale(crossShopButtonImage, (50, 50))

spaceShipsShopListImage = []
for i in range(3):
    spaceShipsShopListImage.append(pygame.image.load(f"MENU/SHOP/ship{i}.png"))

chooseButtonImage = pygame.image.load("MENU/SHOP/choose.png")


playerImage = pygame.image.load("GAME/player.png")
playerImage = pygame.transform.scale(playerImage, (100,100))

meteorImage = pygame.image.load("GAME/meteor.png")
meteorImage = pygame.transform.scale(meteorImage, (150,150))

lazerImage = pygame.image.load("GAME/lazer.png")
lazerImage = pygame.transform.scale(lazerImage, (100, 100))

health_path = ["GAME/HEALTH/0.png", "GAME/HEALTH/1.png", "GAME/HEALTH/2.png", "GAME/HEALTH/3.png"]
health_image_list = []


for i in range(4):
    img = pygame.image.load(health_path[i])
    img = pygame.transform.scale(img, (100, 45))
    img.set_colorkey((128,128,12))
    health_image_list.append(img)

# ============================================================================================================
