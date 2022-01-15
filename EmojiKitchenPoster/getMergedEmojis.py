#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import urllib
import requests
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

def getEmojiFileName(index):
    return "%s/%s.png" % (EMOJIS_DIR, getEmojiCode(index))

def getMergedFileName(first, second):
    return "%s/%s_%s.png" % (MERGED_DIR, getEmojiCode(first), getEmojiCode(second))

def downloadMergedFile(first, second):
    code1 = getEmojiCode(first)
    code2 = getEmojiCode(second)

    for date in DATES:
        try:
            try:
                u1 = code1
                u2 = code2
                filename = f"{u1}_{u2}.png"
                link = 'https://www.gstatic.com/android/keyboard/emojikitchen/%s/%s/%s_%s.png' % (date, u1, u1, u2)
                urllib.request.urlretrieve(link, filename)
            except:
                u1 = code2
                u2 = code1
                filename = f"{u1}_{u2}.png"
                link = 'https://www.gstatic.com/android/keyboard/emojikitchen/%s/%s/%s_%s.png' % (date, u1, u1, u2)
                urllib.request.urlretrieve(link, filename)

            return
        except:
            continue

    raise


def main(argc, argv):
    if not os.path.isdir(MERGED_DIR):    
        os.makedirs(MERGED_DIR)

    print('Downloading merged emoji:')

    for i in range(MAX_EMOJI_COUNT):        
        for j in range(i, MAX_EMOJI_COUNT):
            if i == j or i == 0 or j == 0 or os.path.isfile(getMergedFileName(i, j)) or os.path.isfile(getMergedFileName(j, i)):
                continue

            try: 
                print(f"-> ({str(i).zfill(3)}/{str(j).zfill(3)}): {getEmoji(i)} + {getEmoji(j)} - {getEmojiName(i)} + {getEmojiName(j)}")
                downloadMergedFile(i, j)
            except:
                print(f"-> The combination does not exist! ({getMergedFileName(i, j)})")
                continue

            

        # emojiTextFile = open(EMOJIS_TXT, 'r')
        # lines = emojiTextFile.readlines()
        # emojiTextFileLength = len(lines)
        
        # emojiDataList = [ for i, line in enumerate(lines)]

        # for i in range()

        # for i in reversed(range(MAX_EMOJI_COUNT)):
        #     for j in reversed(range(i, MAX_EMOJI_COUNT)):
        #         filename = os.path.join(MERGED_DIR, '%03d_%03d.png' % (i, j))
                
        #         if os.path.isfile(filename):
        #             continue

        #         print('--> (%03d/%03d): [%s] x [%s]' % (i + 1, j + 1, EMOJIS[i][0], EMOJIS[j][0]))
                
        #         code1 = '-'.join(['u%s' % code for code in EMOJIS[i][2]])
        #         code2 = '-'.join(['u%s' % code for code in EMOJIS[j][2]])
        #         links = []

        #         try: 
        #             
        #         except:
        #             for link in links:
        #                 print('--> Failed: %s' % link)

        # print('Downloading merged emoji complete!')

if __name__ == '__main__':
   main(len(sys.argv) - 1, sys.argv[1:])