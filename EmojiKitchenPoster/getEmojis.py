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
    emojiSVGLink = 'https://raw.githubusercontent.com/googlefonts/noto-emoji/main/svg/emoji_%s.svg'
    emojiTextFile = open(EMOJIS_TXT, 'r')
    lines = emojiTextFile.readlines()
    emojiTextFileLength = len(lines)
    exceptions = { f'u{emoji[2][0]}' : emoji for emoji in EMOJI_EXCEPTIONS }
    exceptionsSeen = 0

    for i, line in enumerate(lines):
        components = line.split(',')
        
        # If emojis.txt already has the data for that emoji, try to get it.
        if len(components) == 3:
            emoji, fileCode, name = components
            emojiSVGFilename = f'{EMOJIS_DIR}/{fileCode}.svg'
            
            if not os.path.isfile(emojiSVGFilename):
                try:
                    print(f'-> Getting ({"%03d" % i}/{emojiTextFileLength - 1}): {emoji} {f"u{ord(emoji)}"} {name[:-1]}')
                    
                    try:    
                        urllib.request.urlretrieve(emojiSVGLink % fileCode.replace('-ufe0f', '').replace('-u', '_'), emojiSVGFilename)
                    except:
                        urllib.request.urlretrieve(emojiSVGLink % fileCode.replace('-u', '_'), emojiSVGFilename)
                except:
                    print('Failed to download emoji svg.')
                    return
        # Otherwise get the emojis and build up emojis.txt with the data.
        else:
            emoji = line[0]
            code = f'u{ord(emoji):x}'
            name = unicodedata.name(emoji)
            emojiData += f'{emoji},{code},{name}\n'
            emojiSVGFilename = f'{EMOJIS_DIR}/{code}.svg'

            if not os.path.isfile(emojiSVGFilename):
                try:
                    print(f'-> Getting ({"%03d" % (i + exceptionsSeen)}/{emojiTextFileLength + len(EMOJI_EXCEPTIONS) - 1}): {name}')
                    urllib.request.urlretrieve(emojiSVGLink % code, emojiSVGFilename)
                except:
                    print('Failed to download emoji svg.')
                    return

            if code in exceptions:
                exceptionsSeen += 1
                exception = exceptions[code] 
                exceptionCode = f'u{"-u".join(exception[2])}'
                exceptionCodeForLink = f'u{"_".join(exception[2])}'
                exceptionName = exception[0]
                emojiData += f'{EXCEPTION_CHAR},{exceptionCode},{exceptionName}\n'
                exceptionSVGFilename = f'{EMOJIS_DIR}/{exceptionCode}.svg'

                if not os.path.isfile(exceptionSVGFilename):
                    try:
                        print(f'-> Getting ({"%03d" % (i + exceptionsSeen)}/{emojiTextFileLength + len(EMOJI_EXCEPTIONS) - 1}): {exceptionName.upper()}')
                        urllib.request.urlretrieve(emojiSVGLink % exceptionCodeForLink, exceptionSVGFilename)
                    except:
                        print('Failed to download emoji svg.')
                        return

    print('-> Complete!')

    if emojiData != '':
        print('Copying name data to emojis.txt.')

        emojiTextFile = open(EMOJIS_TXT, 'w')
        emojiTextFile.write(emojiData)

if __name__ == '__main__':
   main(len(sys.argv) - 1, sys.argv[1:])
