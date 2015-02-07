#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from pygame.locals import *



from lib import *
from key import listen


class Ship:
    sprite = load_entity_sprite('media/ship.png')

    def __init__(self, pos, speed=1):
        self.pos = pos
        self.lasers = []
        self.last_canon_that_fired = random.choice((-1, 1))
        self.speed = speed

    @property
    def pos(self):
        return self.x, self.y

    @pos.setter
    def pos(self, newpos):
        self.x, self.y = newpos

    def shift(self, dx):
        x = self.x + dx
        if 0 <= x <= SCREEN_WIDTH - ENTITY_WIDTH:
            self.x = x

    @listen(K_LEFT)
    def shift_left(self):
        self.shift(-self.speed)

    @listen(K_RIGHT)
    def shift_right(self):
        self.shift(self.speed)

    @listen(K_SPACE, 40)
    def fire(self):

        dx = (self.last_canon_that_fired == -1) * (ENTITY_WIDTH - 3) + 1

        self.lasers.append(
            Laser(
                self.x + dx,
                self.y, random.uniform(0.7, 1.5)
            )
        )

        self.last_canon_that_fired *= -1


class Laser:
    def __init__(self, x, y, velocity=.9):
        self.x, self.y = x, y
        self.velocity = velocity

    @property
    def pos(self):
        return self.x, self.y

    @pos.setter
    def pos(self, newpos):
        self.x, self.y = newpos

    def move_up(self):
        self.y -= self.velocity