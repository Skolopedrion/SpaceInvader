#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

    def update(self, game):
        for invader_index, invader in enumerate(self):
            invader.y += .1

            for laser_index, laser in enumerate(game.ship.lasers):
                if int(laser.x) in range(*invader.mask[0]) and int(laser.y) in range(*invader.mask[1]):
                    del game.ship.lasers[laser_index]
                    del self[invader_index]
                    break

    def persists(self):
        return bool(self)