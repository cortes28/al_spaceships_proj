import pygame as pg
from laser import LaserType
import time


class Sound:
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer.music.load(bg_music)
        # depends on how it sounds on your end, update here
        pg.mixer.music.set_volume(0.01)
        alienlaser_sound = pg.mixer.Sound('sounds/al_laser.wav')
        alienlaser_sound.set_volume(0.02)
        photontorpedo_sound = pg.mixer.Sound('sounds/ship_laser.wav')
        photontorpedo_sound.set_volume(0.03)
        gameover_sound = pg.mixer.Sound('sounds/game_over.wav')
        self.sounds = {'alienlaser': alienlaser_sound, 'photontorpedo': photontorpedo_sound,
                       'gameover': gameover_sound}

    def play_bg(self):
        pg.mixer.music.play(-1, 0.0)

    def stop_bg(self):
        pg.mixer.music.stop()

    def shoot_laser(self, type): 
        pg.mixer.Sound.play(self.sounds['alienlaser' if type == LaserType.ALIEN else 'photontorpedo'])
    def gameover(self): 
        self.stop_bg() 
        pg.mixer.music.load('sounds/game_over.wav')
        self.play_bg()
        time.sleep(4)
