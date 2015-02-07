#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib import load_entity_sprite


class Invader:
    green = load_entity_sprite('media/invader_green.png')
    blue = load_entity_sprite('media/invader_blue.png')
    red = load_entity_sprite('media/invader_red.png')

    def __init__(self, pos, sprite):
        self.x, self.y = pos
        self.sprite = sprite

    @property
    def pos(self):
        return self.x, self.y

    @pos.setter
    def pos(self, newpos):
        self.x, self.y = newpos

    @property
    def mask(self):
        return (
            (
                int(self.pos[0]),
                int(self.pos[0] + self.sprite.get_rect()[2])
            ),
            (
                int(self.pos[1]),
                int(self.pos[1] + self.sprite.get_rect()[3])
            )
        )