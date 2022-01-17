#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import urllib
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
CHUNK_SIZE = 1

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def reduce(results):
    return functools.reduce(lambda x, y: x or y, results)

def getEmoji(index):
    return EMOJIS[index][0]

def getEmojiCode(index):
    return EMOJIS[index][1]

def getEmojiName(index):
    return EMOJIS[index][2]

def getEmojiDate(index):
    return EMOJIS[index][3]

def getEmojiFileName(index):
    return "%s/%s.png" % (EMOJIS_DIR, getEmojiCode(index))

def getMergedFileName(first, second):
    return "%s/%s_%s.png" % (MERGED_DIR, getEmojiCode(first), getEmojiCode(second))

async def downloadFile(date, u1, u2):
    filename = f"{u1}_{u2}.png"
    link = 'https://www.gstatic.com/android/keyboard/emojikitchen/%s/%s/%s_%s.png' % (date, u1, u1, u2)

    try:
        urllib.request.urlretrieve(link, f"{MERGED_DIR}/{filename}")
        return True
    except:
        return False


async def downloadMergedFile(first, second):
    results = await asyncio.gather(
        *[downloadFile(date, getEmojiCode(first), getEmojiCode(second)) for date in DATES]
    )

    return reduce(results)

async def checkAndDownloadMergedFile(a, b):
    if os.path.isfile(getMergedFileName(a, b)) or os.path.isfile(getMergedFileName(b, a)):
        return (-1, True)
    
    if "" not in [getEmojiDate(a), getEmojiDate(b)]:
        first, second = (a, b) if getEmojiDate(a) >= getEmojiDate(b) else (b, a)

        return (b, await downloadFile(getEmojiDate(first), getEmojiCode(first), getEmojiCode(second)))

    results = await asyncio.gather(
        *[downloadMergedFile(first, second) for first, second in [(a, b), (b, a)]]
    )       

    return (b, reduce(results))

async def main(argc, argv):
    if not os.path.isdir(MERGED_DIR):    
        os.makedirs(MERGED_DIR)

    print('Downloading merged emoji:')

    for a in range(MAX_EMOJI_COUNT):        
        for chunk in chunker(range(a, MAX_EMOJI_COUNT), CHUNK_SIZE):
            results = await asyncio.gather(
                *[checkAndDownloadMergedFile(a, b) for b in chunk]
            )

            for b, result in results:
                if b == -1:
                    continue
                
                print(f"-> ({str(a).zfill(3)}/{str(b).zfill(3)}): {getEmoji(a)} + {getEmoji(b)} - {getEmojiName(a)} + {getEmojiName(b)}")
                
                if not result:
                    print(f"XX The combination does not exist!")
    
    print('Downloading merged emoji complete!')

if __name__ == '__main__':
   asyncio.run(main(len(sys.argv) - 1, sys.argv[1:]))
