#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg
from pygame.locals import *
from collections import defaultdict

from constants import *

pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)

from ship import Ship
from wave import Wave
from fpscounter import FPSCounter


class Game:
    background = pg.transform.scale(
        pg.image.load('media/space.png'), SCREEN_SIZE
    )

    game_over = pg.transform.scale(pg.image.load('media/game_over.png').convert_alpha(), (SCREEN_WIDTH // 2, SCREEN_WIDTH // 2))

    def __init__(self):
        self.ship = Ship(
            pos=(
                SCREEN_WIDTH // 2 - ENTITY_WIDTH // 2,
                SCREEN_HEIGHT - ENTITY_HEIGHT - 16
            )
        )
        self.waves = [Wave.generate(9, y) for y in range(3, 13)]
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
        fpscounter = FPSCounter(clock)
        running = True

        while running and self.waves:
            dt = clock.tick()

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

            self.process_key(dt)

            self.waves[0].update(self, dt)
            self.ship.update(dt)

            if not self.waves[0]:
                self.waves.pop(0)

            for i, laser in enumerate(self.ship.lasers):
                laser.move_up(dt)
                if laser.rect.y <= 0:
                    del self.ship.lasers[i]

            fpscounter.update(dt)

            self.draw()
            fpscounter.draw(screen)

            pg.display.flip()

        pg.quit()

    def draw(self):
        screen.blit(Game.background, (0, 0))

        for laser in self.ship.lasers:
            screen.blit(laser.surface, laser.pos)

        for invader in self.waves[0]:
            screen.blit(invader.sprite, invader.pos)

        screen.blit(Ship.sprite, self.ship.pos)

    def over(self):
        screen.blit(
            Game.game_over,
            (
                SCREEN_WIDTH // 2 - Game.game_over.get_width() // 2,
                SCREEN_HEIGHT // 2 - Game.game_over.get_height() // 2,
            )
        )
        pg.display.flip()