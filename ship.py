#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from pygame.locals import *

from lib import *


class Ship:
    sprite = load_entity_sprite('media/ship.png')

    def __init__(self, pos, speed=50, fire_rate=2):
        self.pos = pos
        self.lasers = []
        self.last_canon_that_fired = random.choice((-1, 1))
        self.speed = speed
        self.laser_cooldown = 0
        self.fire_rate = fire_rate

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
    def __init__(self, x, y, velocity=200):
        self.x, self.y = x, y
        self.velocity = velocity

    @property
    def pos(self):
        return self.x, self.y

    @pos.setter
    def pos(self, newpos):
        self.x, self.y = newpos

    def move_up(self, dt):
        self.y -= self.velocity * dt / 1000