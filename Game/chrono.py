
import pygame
import setting

class Chrono:

    def __init__(self, position):
        self.m1 = 0
        self.m2 = 0
        self.s1 = 0
        self.s2 = 0
        self.secondTime = 0
    
        self.frame = 0
        self.max_frame_per_second = setting.fps

        self.work = False
        self.position = position

        self.font = pygame.font.SysFont("Arial", 30)
    

    def start(self):
        self.work = True
    
    def restart(self):
        self.m1 = 0
        self.m2 = 0
        self.s1 = 0
        self.s2 = 0
        self.secondTime = 0

    def updateTime(self):
        if self.work:
            self.frame += 1

            if self.frame == self.max_frame_per_second:
                self.frame = 0
                self.secondTime += 1

                self.s2 += 1
                if self.s2 == 10:
                    self.s2 = 0
                    self.s1 += 1
                    if self.s1 == 6:
                        self.s1 = 0
                        self.m2 += 1
                        if self.m2 == 10:
                            self.m2 = 0
                            self.m1 += 1
    
    def showChrono(self, window): 
        timeWritten = "{}{}:{}{}".format(self.m1, self.m2, self.s1, self.s2)
        time = self.font.render(timeWritten, True, (255,255,255))

        window.blit(time, self.position)
    
    def getSTime(self):
        return self.secondTime