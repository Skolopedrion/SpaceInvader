#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from constants import *
from game import Game
from ship import Ship
from wave import Wave


def main():
    ship = Ship(
        pos=(
            SCREEN_WIDTH // 2 - ENTITY_WIDTH // 2,
            SCREEN_HEIGHT - ENTITY_HEIGHT - 16
        )
    )
    game = Game(ship, [Wave.generate(9, y) for y in range(3, 13)])

    game.mainloop()

if __name__ == '__main__':
    main()
