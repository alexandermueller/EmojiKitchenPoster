#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from Constants import *
from PIL import Image, ImageDraw, ImageFont
    
def clamp(minVal, val, maxVal):
    return max(minVal, min(val, maxVal))

def emojiText(index):
    return "%03d" % index

def emojiFileName(index):
    return "%s/%s.png" % (EMOJIS_DIR, emojiText(index))

def mergedText(first, second):
    return "%03d_%03d" % (first, second)

def mergedFileName(first, second):
    return "%s/%s.png" % (MERGED_DIR, mergedText(first, second))

def main(argc, argv):
    print("Preparing poster file...")
    
    font = ImageFont.truetype(FONT_TYPE, FONT_SIZE)
    rows = MAX_EMOJI_COUNT
    columns = MAX_EMOJI_COUNT

    startRow = 0
    startColumn = 0

    if argc == 2:
        columns, rows = [clamp(1, int(i), MAX_EMOJI_COUNT) if i.isnumeric() else MAX_EMOJI_COUNT for i in argv]

    if argc == 4:
        startColumn, startRow = [clamp(0, int(argv[i * 2]) - 1, MAX_EMOJI_COUNT) if argv[i * 2] else MAX_EMOJI_COUNT for i in range(2)]
        columns, rows = [clamp(1, int(argv[i * 2 + 1]), MAX_EMOJI_COUNT) if argv[i * 2 + 1] else MAX_EMOJI_COUNT for i in range(2)]

    # background = Image.open("./Assets/background.png").convert("RGBA")
    finalW, finalH = (SPRITE_WIDTH * (columns + 1), SPRITE_HEIGHT * (rows + 1) + BOTTOM_DELTA)
    final = Image.new("RGBA", (finalW, finalH))
    draw = ImageDraw.Draw(final)
    
    if not os.path.exists(POSTER_DIR):
        os.makedirs(POSTER_DIR)

    # Draw background first
    # print("Adding background...")
    
    # origin = Image.open("./Assets/origin.png").convert("RGBA")
    # final.paste(origin, (0, 0, 340, 340))

    # for i in range(columns + 1):
    #     for j in range(rows + 1):
    #         x, y = (i * SPRITE_WIDTH, j * SPRITE_HEIGHT)
    #         final.paste(background, (x, y, x + SPRITE_WIDTH, y + SPRITE_HEIGHT))

    # cellWidth = background.size[0]
    # croppedCell = background.crop((0, 0, cellWidth, BOTTOM_DELTA))
    
    # for i in range(columns + 1):
    #     x, y = (SPRITE_WIDTH * i, SPRITE_HEIGHT * (rows + 1))
    #     final.paste(croppedCell, (x, y, x + cellWidth, y + BOTTOM_DELTA))

    # Plop origin cell down

    # origin = Image.open("./Assets/origin.png").convert("RGBA")
    # final.paste(origin, (0, 0, 340, 340))
    
    # Draw sprites and text
    
    maxLineLength = 0

    for i in range(startColumn, min(startColumn + columns, MAX_EMOJI_COUNT) + 1):
        for j in range(startRow, min(startRow + rows, MAX_EMOJI_COUNT) + 1):
            if not (i == startColumn and j == startRow):
                emojiName = ""
                fileName = ""
                first = 0
                second = 0
                fill = WHITE_FILL

                if i == startColumn or j == startRow:
                    fill = RED_FILL
                    index = (j if i == startColumn else i) - 1
                    text = emojiName = emojiText(index)
                    fileName = emojiFileName(index)
                else:
                    if i == j:
                        fill = RED_FILL
                    
                    iIndex = i - 1
                    jIndex = j - 1

                    if not os.path.isfile(mergedFileName(iIndex, jIndex)):
                        if not os.path.isfile(mergedFileName(jIndex, iIndex)):
                            continue

                        first = jIndex
                        second = iIndex
                    else:
                        first = iIndex
                        second = jIndex

                    text = emojiName = mergedText(first, second)
                    fileName = mergedFileName(first, second)

                print("Adding Sprite: %s" % (emojiName))

                current = Image.open(fileName).convert("RGBA")

                x, y = (SPRITE_WIDTH * (i - startColumn), SPRITE_HEIGHT * (j - startRow))
                width, height = current.size
                deltaX, deltaY = (round((SPRITE_WIDTH - width) / 2), round((SPRITE_HEIGHT - height) / 2))
      
                final.paste(current, (x + deltaX, y + deltaY, x + deltaX + width, y + deltaY + height), current)
                                   
                w, h = draw.textsize(text, font=font)
                draw.text((x + (SPRITE_WIDTH - w) / 2, y + (SPRITE_HEIGHT - 33)), text, fill=fill, font=font)

    # Finally, draw credits

    credits = "「EmojiKitchenPoster 2021 | Alex Mueller」"
    f = ImageFont.truetype(FONT_TYPE, int(FONT_SIZE * 2 / 5))
    w, h = draw.textsize(credits, font=f)
    delta = (BOTTOM_DELTA - h) / 2
    x, y = ((finalW - w) / 2, finalH - h - delta)
    draw.text((x, y), credits, fill=(150, 150, 150, 255), font=f)

    print("Saving...", flush=True)
    final.save('%s/EmojiKitchenPoster(%ix%i)[rowStart=%s, columnStart=%s].png' % (POSTER_DIR, columns, rows, startRow, startColumn))
    print("Finished!")

if __name__ == '__main__':
   main(len(sys.argv) - 1, sys.argv[1:])