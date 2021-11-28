#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ASSETS_DIR = './Assets'
POSTER_DIR = '%s/Poster' % ASSETS_DIR
MERGED_DIR = '%s/Merged' % ASSETS_DIR
RENAMED_DIR = '%s/Renamed' % ASSETS_DIR
EMOJIS_DIR = '%s/Emojis' % ASSETS_DIR
EMOJIS_TXT = '%s/emojis.txt' % ASSETS_DIR

SPRITE_WIDTH, SPRITE_HEIGHT = (600, 600)
BOTTOM_DELTA = 75
FONT_SIZE = 30
FONT_TYPE = 'arial-unicode-ms.ttf'

RED_FILL = (255, 0, 0, 255)
WHITE_FILL = (255, 255, 255, 255)
BLACK_FILL = (0, 0, 0, 255)

EMOJI_EXCEPTIONS = [       
    ("FACE EXHALING", "20210218", ["1f62e","200d", "1f4a8"]),
    ("FACE IN CLOUDS", "20210218", ["1f636", "200d", "1f32b"]),
    ("MENDING HEART", "20210218", ["2764", "200d", "1fa79"]),
]

EXCEPTION_CHAR = "x"