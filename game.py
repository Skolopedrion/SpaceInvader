#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg
from pygame.locals import *

pg.init()
pg.display.init()

from constants import *
from ship import Ship
from key import Key


class Game:
    screen = pg.display.set_mode(SCREEN_SIZE)
    background = pg.transform.scale(
        pg.image.load('media/space.png'), SCREEN_SIZE
    )

    game_over = pg.transform.scale(pg.image.load('media/game_over.png').convert_alpha(), (SCREEN_WIDTH // 2, SCREEN_WIDTH // 2))

    def __init__(self, ship, waves=()):
        self.ship = ship
        self.waves = list(waves)

        self.active = {}

    def update_active(self):
        for key in self.active:
            self.active[key] += 1

    def do(self, key):
        for listened in Key.listened:
            if listened.key == key:
                listened(self.ship, self.active[key])

    def mainloop(self):
        running = True

        while running and self.waves:
            for i, laser in enumerate(self.ship.lasers):
                laser.move_up()
                if laser.y <= 0:
                    del self.ship.lasers[i]

            for key in self.active:
                    self.do(key)

            self.draw()
            pg.display.flip()

            for event in pg.event.get():
                if event.type == KEYDOWN:
                    self.active[event.key] = 0

                    if event.key == K_ESCAPE:
                        running = False
                        break

                elif event.type == KEYUP:
                    del self.active[event.key]

                elif event.type == QUIT:
                    running = False
                    break

            self.update_active()
            self.waves[0].update(self)

            if not self.waves[0]:
                self.waves.pop(0)

        # self.over()
        # pg.time.wait(10000)

        pg.quit()

    def draw(self):
        Game.screen.blit(Game.background, (0, 0))

        for laser in self.ship.lasers:
            pg.draw.ellipse(Game.screen, 0xFFFFFF, laser.pos + (2, 10))

        for invader in self.waves[0]:
            Game.screen.blit(invader.sprite, invader.pos)

        Game.screen.blit(Ship.sprite, self.ship.pos)

    def over(self):
        Game.screen.blit(
            Game.game_over,
            (
                SCREEN_WIDTH // 2 - Game.game_over.get_width() // 2,
                SCREEN_HEIGHT // 2 - Game.game_over.get_height() // 2,
            )
        )
        pg.display.flip()