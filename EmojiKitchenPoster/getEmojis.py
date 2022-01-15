#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import urllib
import requests
import unicodedata
from lxml import html
from Constants import *

# conversion bash script: 
# for file in *; do inkscape -w 534 -h 534 "${file}" -o "${file/svg/png}"; done

def main(argc, argv):
    if not os.path.isdir(EMOJIS_DIR):
        os.makedirs(EMOJIS_DIR)

    print('Downloading emoji list...')
    
    if not os.path.isfile(EMOJIS_TXT):
        emojiTextLink = 'https://raw.githubusercontent.com/UCYT5040/Google-Sticker-Mashup-Research/main/emojis.txt'

        try:
            urllib.request.urlretrieve(emojiTextLink, EMOJIS_TXT)
        except:
            print('Failed to download emoji list.')
            return

    print('Retrieving missing emoji svg files:')

    emojiData = ''
    emojiSVGLink = 'https://raw.githubusercontent.com/googlefonts/noto-emoji/main/svg/emoji_%s.svg' # Also check out KeyboardCool 
    emojiTextFile = open(EMOJIS_TXT, 'r')
    lines = emojiTextFile.readlines()
    emojiTextFileLength = len(lines)

    for i, line in enumerate(lines):
        components = line.split(',')
        
        # If emojis.txt already has the data for that emoji, try to get it.
        if len(components) == 3:
            emoji, fileCode, name = components
            emojiName = name[:-1]
            emojiSVGFilename = f'{EMOJIS_DIR}/{fileCode}.svg'
            
            if not os.path.isfile(emojiSVGFilename):
                try:
                    print(f'-> Getting ({"%03d" % i}/{emojiTextFileLength - 1}): {emoji} {fileCode} {emojiName}') #f"u{ord(emoji)}"
                    
                    try:    
                        urllib.request.urlretrieve(emojiSVGLink % fileCode.replace('-ufe0f', '').replace('-u', '_'), emojiSVGFilename)
                    except:
                        urllib.request.urlretrieve(emojiSVGLink % fileCode.replace('-u', '_'), emojiSVGFilename)
                except:
                    print(f'XX Failed to download emoji svg: {emoji} {fileCode} {emojiName}')
                    return

    print('-> Complete!')

    if emojiData != '':
        print('Copying name data to emojis.txt.')

        emojiTextFile = open(EMOJIS_TXT, 'w')
        emojiTextFile.write(emojiData)

if __name__ == '__main__':
   main(len(sys.argv) - 1, sys.argv[1:])
