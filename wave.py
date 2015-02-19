#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg
import random

from constants import *
from invader import Invader


class Wave(list):
    def __init__(self, movement_type=None, invaders=()):
        super().__init__(invaders)
        self.movement_type = movement_type

    @classmethod
    def generate(cls, w, h, margin=8):
        wave = Wave()
        sprite = random.choice([Invader.green, Invader.blue, Invader.red])

        for y in range(margin, (ENTITY_HEIGHT + margin) * h, ENTITY_HEIGHT + margin):
            for x in range(margin, (ENTITY_WIDTH + margin) * w, ENTITY_WIDTH + margin):
                wave.append(Invader((x, y - h * (ENTITY_HEIGHT + margin)), sprite))
        return wave

    def update(self, game, dt):
        lasers_rect = list(map(lambda laser: laser.rect, game.ship.lasers))

        for invader_index, invader in enumerate(self):
            invader.y += 30 * dt / 1000

            laser_index = invader.rect.collidelist(lasers_rect)
            if laser_index != -1:
                del game.ship.lasers[laser_index]
                del self[invader_index]

    def persists(self):
        return bool(self)