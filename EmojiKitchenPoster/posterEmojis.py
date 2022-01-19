#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import string
from Constants import *
from PIL import Image, ImageDraw, ImageFont
    
emojiTextFile = open(EMOJIS_TXT, 'r')
lines = emojiTextFile.readlines()
EMOJIS = [line[:-1].split(',') for line in lines]
MAX_EMOJI_COUNT = len(lines)

class DynamicColour:
    def __init__(self, dark, light):
        self.dark = dark
        self.light = light

    def fill(self):
        return self.dark if isDark() else self.light

def clamp(minVal, val, maxVal):
    return max(minVal, min(val, maxVal))

def getEmojiCode(index):
    return EMOJIS[index][1]

def getEmojiName(index):
    return EMOJIS[index][2]

def getEmojiFileName(index):
    return "%s/%s.png" % (EMOJIS_DIR, getEmojiCode(index))

def getMergedFileName(first, second):
    return "%s/%s_%s.png" % (MERGED_DIR, getEmojiCode(first), getEmojiCode(second))

def main(argc, argv):
    print("Preparing poster file...")
    
    textColour = DynamicColour(dark = WHITE_FILL, light = BLACK_FILL)
    niceColour = DynamicColour(dark = RED_FILL, light = RED_FILL)

    font = ImageFont.truetype(FONT_TYPE, int(FONT_SIZE / 2))
    rows = MAX_EMOJI_COUNT
    columns = MAX_EMOJI_COUNT

    startRow = 0
    startColumn = 0

    if argc in [1, 3, 5]:
        setModes(str(argv[-1]).lower())

    if argc in [2, 3]:
        columns, rows = [clamp(1, int(i), MAX_EMOJI_COUNT) if i.isnumeric() else MAX_EMOJI_COUNT for i in argv[:2]]

    if argc in [4, 5]:
        startColumn, startRow = [clamp(0, int(argv[i * 2]) - 1, MAX_EMOJI_COUNT) if argv[i * 2] else MAX_EMOJI_COUNT for i in range(2)]
        columns, rows = [clamp(1, int(argv[i * 2 + 1]), MAX_EMOJI_COUNT) if argv[i * 2 + 1] else MAX_EMOJI_COUNT for i in range(2)]

    background = Image.open(getDynamicBackground()).convert("RGBA")
    finalW, finalH = (SPRITE_WIDTH * (columns + 1), SPRITE_HEIGHT * (rows + 1) + BOTTOM_DELTA)
    final = Image.new("RGBA", (finalW, finalH))
    draw = ImageDraw.Draw(final)
    
    if not os.path.exists(POSTER_DIR):
        os.makedirs(POSTER_DIR)

    # Draw background first
    print("Adding background...")
    
    origin = Image.open(getDynamicOrigin()).convert("RGBA")
    final.paste(origin, (0, 0, SPRITE_WIDTH, SPRITE_HEIGHT))

    for i in range(columns + 1):
        for j in range(rows + 1):
            x, y = (i * SPRITE_WIDTH, j * SPRITE_HEIGHT)
            final.paste(background, (x, y, x + SPRITE_WIDTH, y + SPRITE_HEIGHT))

    cellWidth = background.size[0]
    croppedCell = background.crop((0, 0, cellWidth, BOTTOM_DELTA))
    
    for i in range(columns + 1):
        x, y = (SPRITE_WIDTH * i, SPRITE_HEIGHT * (rows + 1))
        final.paste(croppedCell, (x, y, x + cellWidth, y + BOTTOM_DELTA))

    # Plop origin cell down

    origin = Image.open(getDynamicOrigin()).convert("RGBA")
    final.paste(origin, (0, 0, SPRITE_WIDTH, SPRITE_HEIGHT))
    
    # Draw sprites and text

    for i in range(startColumn, min(startColumn + columns, MAX_EMOJI_COUNT) + 1):
        for j in range(startRow, min(startRow + rows, MAX_EMOJI_COUNT) + 1):
            if not (i == startColumn and j == startRow):
                emojiName = ""
                fileName = ""
                first = 0
                second = 0
                colour = textColour

                if i == startColumn or j == startRow:
                    colour = niceColour
                    index = (j if i == startColumn else i) - 1
                    text = emojiName = getEmojiName(index)
                    fileName = getEmojiFileName(index)
                else:
                    iIndex = i - 1
                    jIndex = j - 1

                    if not os.path.isfile(getMergedFileName(iIndex, jIndex)):
                        if not os.path.isfile(getMergedFileName(jIndex, iIndex)):
                            continue

                        first = jIndex
                        second = iIndex
                    else:
                        first = iIndex
                        second = jIndex

                    text = emojiName = "%s + %s" % (getEmojiName(first), getEmojiName(second))
                    fileName = getMergedFileName(first, second)


                text = string.capwords(text)
                emojiName = string.capwords(emojiName)

                if i == j:
                    colour = niceColour
                    text = emojiName = "%s x 2" % string.capwords(getEmojiName(first))

                print("Adding Sprite (%03d, %03d): %s" % (first, second, emojiName))

                current = Image.open(fileName).convert("RGBA")

                x, y = (SPRITE_WIDTH * (i - startColumn), SPRITE_HEIGHT * (j - startRow))
                width, height = current.size
                deltaX, deltaY = (round((SPRITE_WIDTH - width) / 2), round((SPRITE_HEIGHT - height) / 2))
      
                final.paste(current, (x + deltaX, y + deltaY, x + deltaX + width, y + deltaY + height), current)

                for index, name in enumerate(text.split("+")):
                    w, h = draw.textsize(name, font=font)
                    draw.text((x + (SPRITE_WIDTH - w) / 2, y + (SPRITE_HEIGHT - 33) + (h * index)), name, fill=colour.fill(), font=font)

    # Finally, draw credits

    credits = "「EmojiKitchenPoster 2021 | Alex Mueller」"
    f = ImageFont.truetype(FONT_TYPE, int(FONT_SIZE * 2 / 5))
    w, h = draw.textsize(credits, font=f)
    delta = (BOTTOM_DELTA - h) / 2
    x, y = ((finalW - w) / 2, finalH - h - delta)
    draw.text((x, y), credits, fill=GRAY_FILL, font=f)

    print("Saving...", flush=True)
    final.save('%s/EmojiKitchenPoster(%ix%i)[rowStart=%s, columnStart=%s]_%s.png' % (POSTER_DIR, columns, rows, startRow, startColumn, getModeFolder()))
    print("Finished!")

if __name__ == '__main__':
   main(len(sys.argv) - 1, sys.argv[1:])
   