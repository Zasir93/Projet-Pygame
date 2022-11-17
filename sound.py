import pygame

pygame.init()

class Sounds:
    def __init__(self):
        pass


    def play(self):
        pygame.mixer.music.load("SOUND/bg.mp3")
        pygame.mixer.music.set_volume(100)
        pygame.mixer.music.play(loops=1)


    def shootSound(self):
        pygame.mixer.music.load("SOUND/shootsound.mp3")
        pygame.mixer.music.set_volume(100)
        pygame.mixer.music.play(loops=1)


    def deadSound(self):
        pygame.mixer.music.load("SOUND/deadsound.mp3")
        pygame.mixer.music.set_volume(100)
        pygame.mixer.music.play(loops=1)




