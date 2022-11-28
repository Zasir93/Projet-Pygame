
import pygame
import random

pygame.mixer.init()

class SoundManager():
    """Classe pour gérer le son et les bruitages
    ...Path: chemin de fichier mp3
    """
    def __init__(self):
        self.lostHealthPointPathList = ["SOUND/attention.mp3", "SOUND/nule.mp3", "SOUND/vie.mp3"]
        self.shootSoundPath = "SOUND/shoot.mp3"
        self.shieldSoundPath = "SOUND/shield.mp3"

    def playAttentionSound(self):
        """
            joue le son de la liste
        """
        randomSound = random.randint(0,2)
        pygame.mixer.music.load(self.lostHealthPointPathList[randomSound])
        pygame.mixer.music.set_volume(100)
        pygame.mixer.music.play()

    def playShootSound(self):
        pygame.mixer.music.load(self.shootSoundPath)
        pygame.mixer.music.set_volume(100)
        pygame.mixer.music.play()

    def playShieldSound(self):
        pygame.mixer.music.load(self.shieldSoundPath)
        pygame.mixer.music.set_volume(100)
        pygame.mixer.music.play()




