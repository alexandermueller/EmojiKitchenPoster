#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ASSETS_DIR = './Assets'
POSTER_DIR = '%s/Poster' % ASSETS_DIR
MERGED_DIR = '%s/Merged' % ASSETS_DIR
EMOJIS_DIR = '%s/Emojis' % ASSETS_DIR
EMOJIS_TXT = '%s/emojis.txt' % ASSETS_DIR

SPRITE_WIDTH, SPRITE_HEIGHT = (600, 600)
BOTTOM_DELTA = 75
FONT_SIZE = 30
FONT_TYPE = 'arial-unicode-ms.ttf'

RED_FILL = (255, 0, 0, 255)
WHITE_FILL = (255, 255, 255, 255)
BLACK_FILL = (0, 0, 0, 255)

# TODO: Try assigning each emoji in emojis.txt a date, and
#       compare the two dates to determine the order instead
#       of brute forcing it.
DATES = [20201001, 20210218, 20210521, 20210831, 20211115]
