
import pygame
import setting
import player
import meteor
import background

pygame.init()

# ====================================================================================
window = pygame.display.set_mode(setting.window_size)
pygame.display.set_caption(setting.window_title)

backgroundImage = pygame.image.load("GAME/space.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, setting.window_size)

playerImage = pygame.image.load("GAME/player.png")
playerImage = pygame.transform.scale(playerImage, setting.spaceship_size)

meteorImageList = []


for i in range(3):
    meteorImageList.append(pygame.image.load(f"GAME/meteor{i+1}.png"))
    meteorImageList[i] = pygame.transform.scale(meteorImageList[i], setting.meteor_size)

lazerImage = pygame.image.load("GAME/lazer.png")
lazerImage = pygame.transform.scale(lazerImage, (100, 100))

health_path = ["GAME/HEALTH/0.png", "GAME/HEALTH/1.png", "GAME/HEALTH/2.png", "GAME/HEALTH/3.png"]
health_image_list = []

for i in range(4):
    img = pygame.image.load(health_path[i])
    img = pygame.transform.scale(img, (100, 45))
    img.set_colorkey((128,128,12))
    health_image_list.append(img)

clock = pygame.time.Clock() # horloge

# ====================================================================================

bg = background.BG(backgroundImage)

spaceship = player.Player("Millenium", 3, 1, playerImage, health_image_list, lazerImage)
meteors = []
interval = 1080/5
x = 0

for i in range(5):
    range = (x, x+interval)
    meteors.append(meteor.Meteor(1, meteorImageList, range))
    x += interval

started = True
while started:

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Fin du programme...")
            started = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spaceship.shoot()

    # ===== affichage =============================================================
    bg.show(window)

    spaceship.show(window)
    spaceship.showHealthPoint(window)
    spaceship.showLazers(window)
    for meteor in meteors:
        meteor.show(window)

    bg.showScore(spaceship.score, window)
    # ==============================================================================

    # ===== Action =================================================================
    for meteor in meteors:
        if spaceship.collision(meteor):
            spaceship._health -= 1
            meteor.show_able = False

    for meteor in meteors:
        if spaceship.collisionBullet(meteor):
            spaceship.score += 1
            meteor.set_damage(spaceship._damage_point)

        meteor.is_destroy()

    if spaceship.is_dead():
        print("Explosion")
        started = False
    # ==============================================================================

    # ===== update ===============================================================
    if keys[pygame.K_UP]:
        spaceship.move('u')
    if keys[pygame.K_DOWN]:
        spaceship.move('d')
    if keys[pygame.K_RIGHT]:
        spaceship.move('r')
    if keys[pygame.K_LEFT]:
        spaceship.move('l')

    spaceship.updateLazers()
    for meteor in meteors:
        meteor.update()
    bg.update()
    # ==============================================================================

    pygame.display.flip() # rafraichissement
    clock.tick(setting.fps) # fps

pygame.quit()