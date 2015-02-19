#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg

from lib import load_entity_sprite


class Invader:
    green = load_entity_sprite('media/invader_green.png')
    blue = load_entity_sprite('media/invader_blue.png')
    red = load_entity_sprite('media/invader_red.png')

    def __init__(self, pos, sprite):
        self.rect = pg.Rect(pos, sprite.get_rect().size)
        self.pos = pos
        self.sprite = sprite

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