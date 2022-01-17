#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import asyncio
import requests
import functools
import unicodedata
from lxml import html
from Constants import *

emojiTextFile = open(EMOJIS_TXT, 'r')
lines = emojiTextFile.readlines()
EMOJIS = [line[:-1].split(',') for line in lines]
MAX_EMOJI_COUNT = len(lines)

def getEmoji(index):
    return EMOJIS[index][0]

def getEmojiCode(index):
    return EMOJIS[index][1]

def getEmojiName(index):
    return EMOJIS[index][2]

def getEmojiDate(index):
    return EMOJIS[index][3]

async def isEmojiDate(date, code):
    url = 'https://www.gstatic.com/android/keyboard/emojikitchen/%s/%s/%s_%s.png' % (date, code, code, code)
    response = requests.get(url)
    return (response.status_code == 200, date)

async def fetchEmojiDate(index):
    date = getEmojiDate(index)
    
    if date != "":
        return date
    else:
        results = await asyncio.gather(
            *[isEmojiDate(date, index) for date in DATES]
        )

        return ', '.join(sorted(list(map(lambda x: str(x[1]), list(filter(lambda x: x[0], results))))))

async def main(argc, argv):
    if not os.path.isdir(MERGED_DIR):    
        os.makedirs(MERGED_DIR)

    print('Getting new emoji dates:')

    for i in range(MAX_EMOJI_COUNT): 
        if getEmojiDate(i) != "":
            continue
             
        print(f"-> ({str(i).zfill(3)}): {getEmoji(i)} - {getEmojiName(i)} ({await fetchEmojiDate(i)})")

    print('Complete!')

if __name__ == '__main__':
    asyncio.run(main(len(sys.argv) - 1, sys.argv[1:]))
