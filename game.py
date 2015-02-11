#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg
from pygame.locals import *
from collections import defaultdict

pg.init()
pg.display.init()

from constants import *
from ship import Ship


class Game:
    screen = pg.display.set_mode(SCREEN_SIZE)
    background = pg.transform.scale(
        pg.image.load('media/space.png'), SCREEN_SIZE
    )

    game_over = pg.transform.scale(pg.image.load('media/game_over.png').convert_alpha(), (SCREEN_WIDTH // 2, SCREEN_WIDTH // 2))

    def __init__(self, ship, waves=()):
        self.ship = ship
        self.waves = list(waves)

        self.active = defaultdict(lambda: False)

    def process_key(self, dt):
        if self.active[K_LEFT]:
            self.ship.shift_left(dt)
        if self.active[K_RIGHT]:
            self.ship.shift_right(dt)
        if self.active[K_SPACE]:
            self.ship.fire()

    def mainloop(self):
        clock = pg.time.Clock()
        running = True

        while running and self.waves:
            pg.time.wait(0)
            dt = clock.tick()

            for i, laser in enumerate(self.ship.lasers):
                laser.move_up(dt)
                if laser.y <= 0:
                    del self.ship.lasers[i]

            self.process_key(dt)

            self.draw()
            pg.display.flip()

            for event in pg.event.get():
                if event.type == KEYDOWN:
                    self.active[event.key] = True

                    if event.key == K_ESCAPE:
                        running = False
                        break

                elif event.type == KEYUP:
                    self.active[event.key] = False

                elif event.type == QUIT:
                    running = False
                    break

            self.waves[0].update(self, dt)
            self.ship.update(dt)

            if not self.waves[0]:
                self.waves.pop(0)

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