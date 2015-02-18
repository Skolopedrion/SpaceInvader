#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from pygame.locals import *

from lib import *


class Ship:
    sprite = load_entity_sprite('media/ship.png')

    def __init__(self, pos, speed=50, fire_rate=2):
        self.rect = pg.Rect(pos, self.sprite.get_rect().size)
        self.lasers = []
        self.last_canon_that_fired = random.choice((-1, 1))
        self.speed = speed
        self.laser_cooldown = 0
        self.fire_rate = fire_rate

    @property
    def pos(self):
        return self.rect.topleft

    @pos.setter
    def pos(self, newpos):
        self.rect.topleft = newpos

    def shift(self, dx):
        x = self.rect.x + dx
        if 0 <= x <= SCREEN_WIDTH - ENTITY_WIDTH:
            self.x = x

    def shift_left(self, dt):
        self.shift(-self.speed * dt / 1000)

    def shift_right(self, dt):
        self.shift(self.speed * dt / 1000)

    def fire(self):
        if self.laser_cooldown > 0:
            return

        dx = (self.last_canon_that_fired == -1) * (ENTITY_WIDTH - 3) + 1

        self.lasers.append(
            Laser(
                self.x + dx,
                self.y, random.randint(125, 225)
            )
        )

        self.last_canon_that_fired *= -1

        self.laser_cooldown = 1 / self.fire_rate

    def update(self, dt):
        dt /= 1000
        if self.laser_cooldown > 0:
            self.laser_cooldown = max(0, self.laser_cooldown - dt)


class Laser:
    surface = pg.Surface((2, 10))
    pg.draw.ellipse(surface, 0xFFFFFF, (0, 0, 2, 10))

    def __init__(self, x, y, velocity=200):
        self.rect = pg.Rect((x, y), self.surface.get_rect().size)
        self.velocity = velocity

    @property
    def pos(self):
        return self.rect.topleft

    @pos.setter
    def pos(self, newpos):
        self.rect.topleft = newpos

    def move_up(self, dt):
        self.rect.y -= self.velocity * dt / 1000