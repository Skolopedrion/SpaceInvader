#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *


class FPSCounter:
    """
    FPS Counter class that updates the fps information only once per
    second for better performances.
    You must call its update method every tick.
    """
    def __init__(self, clock):
        """clock is a pygame.time.Clock object"""
        self.clock = clock
        self.text_renderer = pygame.font.Font(pygame.font.get_default_font(), 32)
        self.fps_surface = self.text_renderer.render("0", True, (200, 200, 200, 128))
        self.dt = 0
    
    def update(self, dt):
        """Updates the FPS surface text once every second."""
        self.dt += dt
        if self.dt > 1000:
            self.fps_surface = self.text_renderer.render('{0:.2f}'.format(self.clock.get_fps()), True, (200, 200, 200, 128))
            self.dt = self.dt % 1000
    
    def draw(self, screen_surface):
        """Draws the FPS text onto the given screen_surface."""
        screen_surface.blit(self.fps_surface, (10, 10))

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()
    fps_counter = FPSCounter(clock)

    running = True
    while running:
        dt = clock.tick(50)
        pygame.time.wait(100)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        fps_counter.update(dt)
        
        screen.fill(0)
        fps_counter.draw(screen)
        pygame.display.flip()
        
     
    pygame.quit()
