
import pygame

class Shop:

    def __init__(self, spaceShipList, crossButtonImage, chooseButtonImage):
        self.spaceShipList = spaceShipList
        self.spaceShipListRect = []
        self.currentSpaceShip = 0

        self.surfaceWidth = 720
        self.surfaceHeight = 480

        self.surfaceShop = pygame.Surface((self.surfaceWidth, self.surfaceHeight))

        self.crossButtonImage = crossButtonImage
        self.crossButtonImageRect = self.crossButtonImage.get_rect()

        self.chooseButtonImage = chooseButtonImage
        self.chooseButtonImageRect = self.chooseButtonImage.get_rect()


    def showCrossButton(self):
        self.crossButtonImageRect.x = 720-50-20
        self.crossButtonImageRect.y = 20
        self.surfaceShop.blit(self.crossButtonImage, self.crossButtonImageRect)

    def initSpaceShips(self):

        x = 0
        y = 150
        for i in range(len(self.spaceShipList)):
            self.spaceShipList[i] = pygame.transform.scale(self.spaceShipList[i], (200, 200))
            self.spaceShipListRect.append(self.spaceShipList[i].get_rect())

            x = i * 200 + 30*i + 30
            self.spaceShipListRect[i].x = x
            self.spaceShipListRect[i].y = y


    def showSpaceShips(self):
        for i in range(len(self.spaceShipList)):
            pygame.draw.rect(self.surfaceShop, (0,0,255), self.spaceShipListRect[i], 2)
            self.surfaceShop.blit(self.spaceShipList[i], self.spaceShipListRect[i])

    def showCurrentSpaceShipChoosen(self):
        pygame.draw.rect(self.surfaceShop, (255,255,0), self.spaceShipListRect[self.currentSpaceShip], 3)

    def showChooseButton(self):
        self.chooseButtonImageRect.x = 250
        self.chooseButtonImageRect.y = 380
        self.surfaceShop.blit(self.chooseButtonImage, self.chooseButtonImageRect)

    def showShopWindow(self, window):
        self.surfaceShop.fill((255,255,255))
        rect = pygame.Rect(0, 0, 720, 480)
        #pygame.draw.rect(self.surfaceShop, (255,255,0), rect, 10)
        self.showCrossButton()
        self.showSpaceShips()
        self.showCurrentSpaceShipChoosen()
        self.showChooseButton()

        window.blit(self.surfaceShop, ((1080-720)/2, (720-480)/2))


    def checkChoice(self):
        pos = pygame.mouse.get_pos()
        rect = pygame.Rect(0,0,200,200)
        for i in range(len(self.spaceShipList)):
            rect.x = self.spaceShipListRect[i].x + (1080-720)/2
            rect.y = self.spaceShipListRect[i].y + (720-480)/2
            if rect.collidepoint(pos):
                self.currentSpaceShip = i

    def isCrossButtonClick(self):
        pos = pygame.mouse.get_pos()
        rect = pygame.Rect(0,0,self.crossButtonImageRect.w,self.crossButtonImageRect.h)
        rect.x = self.crossButtonImageRect.x + (1080-720)/2
        rect.y = self.crossButtonImageRect.y + (720-480)/2

        return rect.collidepoint(pos)

    def isChooseButtonClick(self):
        pos = pygame.mouse.get_pos()
        rect = pygame.Rect(0,0,self.chooseButtonImageRect.w,self.chooseButtonImageRect.h)
        rect.x = self.chooseButtonImageRect.x + (1080-720)/2
        rect.y = self.chooseButtonImageRect.y + (720-480)/2

        return rect.collidepoint(pos)

    def getSpaceshipChoosen(self):
        return self.spaceShipList[self.currentSpaceShip]
