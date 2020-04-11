''' Rahul Shah

    Pong modular form

    4/5/20
'''


import pygame as pg
from pong_settings import *
from pygame.locals import *
from pong_paddle import *
from sys import exit
from Vector2 import Vector2


class Pong:
    def __init__(self):
        # init game window
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)
        pg.display.set_caption(TITLE)
        self.font = pg.font.Font(FONTNAME, FONTSIZE)
        self.bg_img = img
        self.bg = pg.image.load(self.bg_img)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # new game starts
        self.sprites = pg.sprite.Group()
        self.paddles = Paddle()
        self.sprites.add(self.paddles)
        
    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game loop - update
        self.sprites.update()

    def events(self):
        # Game loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

    def draw(self):
        # Game loop - draw
        self.screen.blit(self.bg, (0,0))
        #self.sprites.draw(self.screen)
        pg.draw.rect(self.screen, WHITE, self.paddles.paddle_left_rect)
        pg.draw.rect(self.screen, WHITE, self.paddles.paddle_right_rect)
        pg.display.update()

    def start_screen(self):
        # Click mouse text
        click_mouse_surf = self.font.render("Click mouse to start", True, WHITE, BLACK)
        click_mouse_rect = click_mouse_surf.get_rect()
        click_mouse_rect.center = (WIDTH / 2, (HEIGHT / 2) + 100)
        # PONG screen text
        pong_surf = self.font.render("P O N G", True, WHITE, BLACK)
        pong_rect = pong_surf.get_rect()
        pong_rect.center = (WIDTH / 2, (HEIGHT / 2) - 100)

        self.screen.fill(BLACK)
        self.screen.blit(click_mouse_surf, click_mouse_rect)
        self.screen.blit(pong_surf, pong_rect)

        while not self.check_mouse():
            pg.display.update()

    def end_screen(self):
        pass

    def check_mouse(self):
        for event in pg.event.get():
            return event.type == MOUSEBUTTONDOWN


def main():
    pong = Pong()
    pong.start_screen()
    while pong.running:
        pong.new()
        pong.run()
        pong.end_screen()
    

if __name__ == "__main__":
    main()
