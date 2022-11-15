import pygame

class Sound:
    def __init__(self): 
        self.music = pygame.mixer_music.load("SOUND/bgsound.mp3")
        self.music_volume = pygame.mixer.music.set_volume(0.35)
        self.music_play = pygame.mixer.music.play(loops=-1)
        self.shoot_sound = pygame.mixer.Sound("SOUND/shootsound.wav")
        self.dead_sound = pygame.mixer.Sound("SOUND/deadsound.wav")
        self.sound_volume()

