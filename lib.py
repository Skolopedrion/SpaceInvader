#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg

from constants import *


def load_entity_sprite(path):
    return pg.transform.scale(
        pg.image.load(path).convert_alpha(),
        ENTITY_SIZE
    )