import pygame as pg
from pygame.sprite import Sprite, Group
from timer import Timer

class Barrier(Sprite):
    color = 255, 0, 0
    black = 0, 0, 0


    def __init__(self, game, rect):
        super().__init__()
        self.screen = game.screen
        self.rect = rect
        
        self.settings = game.settings
        self.ship_lasers = game.ship_lasers.lasers
        self.alien_lasers = game.alien_lasers
        self.dying = self.dead = False
        self.opacity = 255          # 255-no transparency at all |||| 0-full transparency
        self.imgo = pg.Surface(self.rect.size, pg.SRCALPHA)

        
        # self.settings = game.settings
        # self.image = pg.image.load('images/alien0.bmp')
        # self.rect = self.image.get_rect()
        # self.rect.y = self.rect.height
        # self.x = float(self.rect.x)
  
    def hit(self):  #pass

        if not self.dying:
            if self.opacity > 0:
                self.opacity = max(self.opacity - 45, 0)
            else:
                self.dying = self.dead = True



    def update(self): self.draw()
    def draw(self): 
        self.imgo.fill((255, 0 ,0, self.opacity))
        # self.rect.blit(self.imgo, (0,0), special_flags = pg.BLEND_RGBA_MULT)
        #pg.draw.rect(self.screen, Barrier.color, self.rect, 0, 20)
        # size = self.rect.size
        # #rect_imag = self.imgo
        # pg.draw.rect(self.imgo, (255, 0, 0), (0, 0, *size), border_radius= 2)
        # self.screen = self.screen.copy().convert_alpha()
        # self.screen.blit(self.imgo, (0, 0), None, pg.BLEND_RGBA_MIN)
        #
        self.screen.blit(self.imgo, self.rect)
        pg.draw.circle(self.screen, self.settings.bg_color, (self.rect.centerx, self.rect.bottom), self.rect.width/6)
        pg.draw.circle(self.screen, self.settings.bg_color, (self.rect.topright), self.rect.width/8)
        pg.draw.circle(self.screen, self.settings.bg_color, (self.rect.topleft), self.rect.width/8)

class Barriers:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.ship_lasers = game.ship_lasers.lasers
        self.alien_lasers = game.alien_lasers
        self.create_barriers()

    def create_barriers(self):     
        width = self.settings.screen_width / 10
        height = 2.0 * width / 4.0
        top = self.settings.screen_height - 2.1 * height
        rects = [pg.Rect(x * 2 * width + 1.5 * width, top, width, height) for x in range(4)]   # SP w  3w  5w  7w  SP
        self.barriers = [Barrier(game=self.game, rect=rects[i]) for i in range(4)]

    # def hit(self): pass 
    
    def reset(self):
        self.create_barriers()

    def update(self):
        self.check_collisions()
        for barrier in self.barriers:
            if barrier.dead == True:
                self.barriers.remove(barrier)

        for barrier in self.barriers: barrier.update()


    # add this func. to update in the same class
    def check_collisions(self): #pass
        collisions = pg.sprite.groupcollide(self.barriers, self.ship_lasers, False, True)
        if collisions:
            for barrier in collisions:
                pass
                barrier.hit()       # implement this

        collisions = pg.sprite.groupcollide(self.barriers, self.alien_lasers.lasers, False, True)
        if collisions:
            for barrier in collisions:
                pass
                barrier.hit()       # implement this         
    def draw(self):
        for barrier in self.barriers: barrier.draw()

