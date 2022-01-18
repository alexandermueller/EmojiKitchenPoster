#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ASSETS_DIR = './Assets'
POSTER_DIR = '%s/Poster' % ASSETS_DIR
MERGED_DIR = '%s/Merged' % ASSETS_DIR
EMOJIS_DIR = '%s/Emojis' % ASSETS_DIR
EMOJIS_TXT = '%s/emojis.txt' % ASSETS_DIR
DYNAMIC_DIR = '%s/Dynamic' % ASSETS_DIR

DATES = [20201001, 20210218, 20210521, 20210831, 20211115]

SPRITE_WIDTH, SPRITE_HEIGHT = (600, 600)
BOTTOM_DELTA = 75
FONT_SIZE = 30
FONT_TYPE = 'arial-unicode-ms.ttf'

IS_DARK = False
IS_CLEAR = False

def isDark():
    return IS_DARK

def setModes(arg):
    global IS_DARK, IS_CLEAR

    IS_DARK = 'dark' in arg
    IS_CLEAR = 'clear' in arg

def getModeFolder():
    return "Clear" if IS_CLEAR else "Dark" if IS_DARK else "Light"

def getDynamicBackground():
    return "%s/%s/background.png" % (DYNAMIC_DIR, getModeFolder())

def getDynamicOrigin():
    return "%s/%s/origin.png" % (DYNAMIC_DIR, getModeFolder())

RED_FILL = (255, 0, 0, 255)
ORANGE_FILL = (255, 121, 0, 255)
BLUE_FILL = (0, 201, 255)
PURPLE_FILL = (175, 0, 255, 255)
WHITE_FILL = (255, 255, 255, 255)
BLACK_FILL = (0, 0, 0, 255)
GRAY_FILL = (150, 150, 150, 255)
