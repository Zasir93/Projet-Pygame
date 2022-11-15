
import pygame

class Menu:

    def __init__(self, imageBG, imageButton, imageShop, imageMoves, imageSpace, imageTitle, shopManager):
        self.imageBG = imageBG
        self.imageButton = imageButton
        self.imageShop = imageShop
        self.imageMoves = imageMoves
        self.imageSpace = imageSpace
        self.imageTitle = imageTitle

        self.imageButtonRect = self.imageButton.get_rect()
        self.imageShopRect = self.imageShop.get_rect()
        self.imageMovesRect = self.imageMoves.get_rect()
        self.imageSpaceRect = self.imageSpace.get_rect()
        self.imageTitleRect = self.imageTitle.get_rect()

        self.shopManager = shopManager


    def showBackground(self, window):
        window.blit(self.imageBG, [0,0])

    def showPlayButton(self, window):
        self.imageButtonRect.x = 400
        self.imageButtonRect.y = 375
        #pygame.draw.rect(window, (255,0,0), self.imageButtonRect, 3)
        window.blit(self.imageButton, self.imageButtonRect)

    def showShopButton(self, window):
        self.imageShopRect.x = 400
        self.imageShopRect.y = 500
        #pygame.draw.rect(window, (255,0,0), self.imageShopRect, 3)
        window.blit(self.imageShop, self.imageShopRect)

    def isPlayButtonClick(self):
        pos = pygame.mouse.get_pos()
        return self.imageButtonRect.collidepoint(pos)

    def showMoves(self, window):
        self.imageMovesRect.x = 20
        self.imageMovesRect.y = 480
        window.blit(self.imageMoves, self.imageMovesRect)

    def showSpace(self, window):
        self.imageMovesRect.x = 730
        self.imageMovesRect.y = 590
        window.blit(self.imageSpace, self.imageMovesRect)

    def showTitle(self, window):
        self.imageTitleRect.x = 5
        self.imageTitleRect.y = -100
        window.blit(self.imageTitle, self.imageTitleRect)

    def isShopButtonClick(self):
        pos = pygame.mouse.get_pos()
        return self.imageShopRect.collidepoint(pos)