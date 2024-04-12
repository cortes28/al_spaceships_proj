from curses import KEY_BACKSPACE, KEY_DOWN
import pygame as pg
from settings import Settings
import game_functions as gf

from laser import Lasers, LaserType
from alien import Aliens
from ship import Ship
from sound import Sound
from scoreboard import Scoreboard
from barrier import Barriers
import sys


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Alien Invasion")
        self.soun = 1

        # file to read the highscore
        text_file = open("highscore.txt", "r")
        self.curr_high_score = text_file.read()
        text_file.close()

        self.sound = Sound(bg_music="sounds/bac_music.mp3")
        

        self.ship_lasers = Lasers(settings=self.settings, type=LaserType.SHIP)
        self.alien_lasers = Lasers(settings=self.settings, type=LaserType.ALIEN)
        
        self.barriers = Barriers(game=self)
        self.ship = Ship(game=self)
        self.scoreboard = Scoreboard(game=self)
        self.aliens = Aliens(game=self)
        self.settings.initialize_speed_settings()
        
    def reset(self):
        print('Resetting game...')
        # self.lasers.reset()
        self.barriers.reset()
        self.ship.reset()
        self.aliens.reset()
        self.scoreboard.reset()

    def game_over(self):
        print('All ships gone: game over!')
        my_file = open("highscore.txt", "w")
        my_file.write(str(self.scoreboard.high_score))
        my_file.close()
        if(self.soun == 1):
            self.soun -= 1
            self.sound.gameover()

        main()

        # if beginning() == True:
        #     cont = True

        # elif beginning() == False:
        #     cont = False


        # if cont:
        #     g = Game()
        #     g.play()
        # else:  
        #     pg.quit()
        #     sys.exit()

    def play(self):
        self.sound.play_bg()
        while True:     # at the moment, only exits in gf.check_events if Ctrl/Cmd-Q pressed
            gf.check_events(settings=self.settings, ship=self.ship)
            self.screen.fill(self.settings.bg_color)
            self.ship.update()
            self.aliens.update()
            self.barriers.update()
            # self.lasers.update()
            self.scoreboard.update()
            pg.display.flip()



def beginning():
    text_file = open("highscore.txt", "r")
    data = text_file.read()
    text_file.close()
    print(data)

    pg.init();
    screen = pg.display.set_mode((740,740));
    pg.display.set_caption("menu");
    menu_active = True;
    # keys=pg.key.get_pressed()

    start_button = pg.draw.rect(screen,(255,0,0),(300,500,100,50));
    #continue_button = pg.draw.rect(screen,(0,244,0),(150,160,100,50));
    #quit_button = pg.draw.rect(screen,(244,0,0),(150,230,100,50));

    color = (255,255,255)
    green = (0,255,0)
    smallfont = pg.font.SysFont('Impact',35)
    text = smallfont.render('START', True, color)
    score = "Highscore: " + str(data)
    high_score = smallfont.render(score, True, color)
    bigfont = pg.font.SysFont('Impact', 70)
    
    space = bigfont.render('SPACE', True, color)
    invaders = bigfont.render('INVADERS', True, green)
    
    screen.blit(space, (250, 100))
    screen.blit(invaders, (210, 160))
    
    space = smallfont.render
    
    screen.blit(text , (305,500))
    screen.blit(high_score, (240, 50))
    
    points1 = smallfont.render(" = 50", True, color)
    screen.blit(points1, (340,250))
    screen.blit(points1, (340,300))
    screen.blit(points1, (340,350))

    Alien1 = pg.image.load('images/alien__00.png')
    Alien2 = pg.image.load('images/alien__10.png')
    Alien3 = pg.image.load('images/alien__20.png')
    
    screen.blit(Alien1, (300, 250))
    screen.blit(Alien2, (300, 300))
    screen.blit(Alien3, (300, 350))

    pg.display.flip();

    def startGame():
        screen.fill((0,0,0));
        pg.display.flip();
        
    def asdf():
        print("hello")

    while menu_active:
        for event in pg.event.get():
            #print(evento);
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # if event.type == pg.KEYDOWN:
            #     if event.key == pg.K_ESCAPE or event.key == pg.K_BACKSPACE:
            #         pg.quit()
            #         sys.exit()

            # if event.type == pg.QUIT or keys[pg.K_ESCAPE] == True or keys[pg.K_BACKSPACE] == True:
            #     pg.quit()
            #     sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pos()[0] >= 300 and pg.mouse.get_pos()[1] >= 500:
                    if pg.mouse.get_pos()[0] <= 350 and pg.mouse.get_pos()[1] <= 550:
                        return True
                        sys.exit()
                        asdf()
                if pg.mouse.get_pos()[0] >= 150 and pg.mouse.get_pos()[1] >= 90:
                    if pg.mouse.get_pos()[0] <= 250 and pg.mouse.get_pos()[1] <= 140:
                        startGame();
                        return True
                        sys.exit()   
def main():

    while True:
        if beginning() == True:
            break

    g = Game()
    g.play()


if __name__ == '__main__':
    main()
