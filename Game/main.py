
import pygame
import setting
import player
import meteor
import background
import menu
import shop
import chrono
import items

pygame.init()

# ====================================================================================
window = pygame.display.set_mode(setting.window_size)
pygame.display.set_caption(setting.window_title)


clock = pygame.time.Clock() # horloge

# ====================================================================================

shopManager = shop.Shop(setting.spaceShipsShopListImage, setting.crossShopButtonImage, setting.chooseButtonImage)
shopManager.initSpaceShips()

home = menu.Menu(setting.menuBackgroundImage, setting.playButtonImage, setting.shopButtonImage,
                setting.imageMoves, setting.imageSpace, setting.imageTitle, shopManager)

bg = background.BG(setting.backgroundImage)

spaceship = player.Player("Millenium", 3, 1, setting.playerImage, setting.health_image_list, setting.lazerImage)
meteors = []
interval = 1080/5
x = 0

for i in range(5):
    range = (x, x+interval)
    meteors.append(meteor.Meteor(1, setting.meteorImage, range))
    x += interval

timer = chrono.Chrono((30, 60))
timer.start()

started = True
while started:

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Fin du programme...")
            started = False


        if event.type == pygame.KEYDOWN:
            if setting.screen == 0:
                if event.key == pygame.K_RETURN:
                    setting.screen = 1

        if event.type == pygame.MOUSEBUTTONDOWN and setting.screen == 0:
            if home.isPlayButtonClick():
                timer.restart()
                setting.screen = 1
            if home.isShopButtonClick():
                setting.screen = 2

        if event.type == pygame.MOUSEBUTTONDOWN and setting.screen == 2:
            home.shopManager.checkChoice()

            if home.shopManager.isCrossButtonClick():
                print("back")
                setting.screen = 0

            if home.shopManager.isChooseButtonClick():
                spaceship.changeSpaceshipSkin(home.shopManager.getSpaceshipChoosen())
                setting.screen = 0


        if event.type == pygame.KEYDOWN and setting.screen == 1:
            if event.key == pygame.K_SPACE:
                spaceship.shoot()
            if event.key == pygame.K_s:
                if spaceship._shield > 0:
                    spaceship._shield_showable = True


    if setting.screen == 0:
        home.showBackground(window)
        home.showPlayButton(window)
        home.showShopButton(window)
        home.showMoves(window)
        home.showSpace(window)
        home.showTitle(window)


    elif setting.screen == 1:
        # ===== affichage =============================================================
        bg.show(window)

        spaceship.show(window)
        spaceship.showHealthPoint(window)
        spaceship.showLazers(window)
        spaceship.showShield(window)
        for meteor in meteors:
            meteor.show(window)

        bg.showScore(spaceship.score, window)
        timer.showChrono(window)
        # ==============================================================================

        # ===== Action =================================================================
        for meteor in meteors:
            if spaceship.collision(meteor):
                spaceship._health -= 1
                meteor.show_able = False

            if spaceship.collisionBullet(meteor):
                spaceship.score += 1
                meteor.set_damage(spaceship._damage_point)
            meteor.levelUp(spaceship.score, timer.getSTime())

            if spaceship.collisionShield(meteor):
                meteor.show_able = False
                spaceship._shield -= 1
                spaceship.stillShield()

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
        timer.updateTime()
        # ==============================================================================

    elif setting.screen == 2:
        home.showBackground(window)
        home.shopManager.showShopWindow(window)


    pygame.display.flip() # rafraichissement
    clock.tick(setting.fps) # fps

pygame.quit()