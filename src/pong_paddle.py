# Pong paddle class

import pygame as pg
from pong_settings import *
from pong_main import *
from pygame.locals import *
from sys import exit
from Vector2 import Vector2

class Paddle(pg.sprite.Sprite):
    def __init__(self):
        # Initalize paddles
        # left paddle
        pg.sprite.Sprite.__init__(self)
        self.paddle_left = pg.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.paddle_left.fill(WHITE)
        self.paddle_left_rect = self.paddle_left.get_rect()
        self.paddle_left_rect.topleft = PADDLE_LEFT_START
        self.left_unit_vec = Vector2(0, 0)
        # right paddle
        self.paddle_right = pg.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.paddle_right.fill(WHITE)
        self.paddle_right_rect = self.paddle_right.get_rect()
        self.paddle_right_rect.topleft = PADDLE_RIGHT_START
        self.right_unit_vec = Vector2(0, 0)
        self.clock = pg.time.Clock()

    def update(self):
        time_sec = self.clock.tick() / 1000

        keys = pg.key.get_pressed()
        if keys[K_w] and not keys[K_s]:
            self.left_unit_vec = Vector2(0, -1)
        if keys[K_s] and not keys[K_w]:
            self.left_unit_vec = Vector2(0, 1)
        if not keys[K_w] and not keys[K_s] or \
            keys[K_s] and keys[K_w]:
            self.left_unit_vec = Vector2(0, 0)

        if keys[K_UP] and not keys[K_DOWN]:
            self.right_unit_vec = Vector2(0, -1)
        if keys[K_DOWN] and not keys[K_UP]:
            self.right_unit_vec = Vector2(0, 1)
        if not keys[K_UP] and not keys[K_DOWN] or \
            keys[K_UP] and keys[K_DOWN]:
            self.right_unit_vec = Vector2(0, 0)


        paddle_dist = time_sec * PADDLE_SPEED
        paddle_left_change = int(self.left_unit_vec[1] * paddle_dist)
        paddle_right_change = int(self.right_unit_vec[1] * paddle_dist)

        self.check_and_change(self.paddle_left_rect, paddle_left_change)
        self.check_and_change(self.paddle_right_rect, paddle_right_change)


    def check_and_change(self, paddle, change):
        if paddle.top + change >= BUFFER and \
            paddle.bottom + change < HEIGHT - BUFFER:
            paddle.top += change


        
