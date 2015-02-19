#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

from lib import *


class Ship:
    sprite = load_entity_sprite('media/ship.png')

    def __init__(self, pos, speed=100, fire_rate=4):
        self.rect = pg.Rect(pos, self.sprite.get_rect().size)
        self.pos = pos
        self.lasers = []
        self.last_canon_that_fired = random.choice((-1, 1))
        self.speed = speed
        self.laser_cooldown = 0
        self.fire_rate = fire_rate

    @property
    def pos(self):
        return self._x, self._y

    @pos.setter
    def pos(self, newpos):
        self._x, self._y = newpos
        self.rect.topleft = newpos

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self.rect.x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self.rect.y = value

    def shift(self, dx):
        self.x += dx
        self.x = max(0, self.x)
        self.x = min(self.x, SCREEN_WIDTH - ENTITY_WIDTH)

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
                self.rect.x + dx,
                self.rect.y, random.randint(125, 225)
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
        self.pos = x, y
        self.velocity = velocity

    @property
    def pos(self):
        return self._x, self._y

    @pos.setter
    def pos(self, newpos):
        self._x, self._y = newpos
        self.rect.topleft = newpos

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self.rect.x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self.rect.y = value

    def move_up(self, dt):
        self.y -= self.velocity * dt / 1000