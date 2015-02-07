#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Key:
    listened = []

    def __init__(self, key, timer=1, action=lambda: None):
        self.key, self.timer = key, timer
        self.action = action

        Key.listened.append(self)

    def __call__(self, obj, idletime):
        if not idletime % self.timer:
            self.action(obj)


def listen(key, timer=1):
    def decorator(fnc):
        return Key(key, timer, fnc)
    return decorator