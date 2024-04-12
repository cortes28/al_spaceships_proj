import pygame as pg 
# import pygame.font

class Scoreboard:
    def __init__(self, game): 
        self.score = 0
        self.level = 0
        self.high_score = int(game.curr_high_score)
        self.game = game
        self.ship = game.ship
        self.ship_imag = pg.image.load('images/ship.png')
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pg.font.SysFont(None, 48)

        self.score_image = None 
        self.score_rect = None
        self.prep_score()
        self.lives()

    def increment_score(self): 
        self.score += self.settings.alien_points
        self.prep_score()

    def prep_score(self): 
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def lives(self):
        lives = str(self.ship.ships_left)
        self.live_img = self.font.render(lives, True, self.text_color, self.settings.bg_color)

        rect = self.ship_imag.get_rect()
        self.screen.blit(self.ship_imag, (30,0))

        self.live_rect = self.live_img.get_rect()
        self.live_rect.left = self.screen_rect.left + 20
        self.live_rect.top = 20

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.update()

    def update(self): 
        # TODO: other stuff
        self.lives()
        self.prep_score()
        self.draw()

    def draw(self): 
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.live_img, self.live_rect)