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
        self.sprite = sprite

    @property
    def pos(self):
        return self.rect.topleft

    @pos.setter
    def pos(self, newpos):
        self.rect.topleft = newpos