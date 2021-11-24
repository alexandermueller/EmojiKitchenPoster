#!/usr/bin/python

from lxml import html
import requests
import urllib
import os
from Constants import *

# conversion bash script: 
# for file in *; do inkscape -w 534 -h 534 "${file}" -o "${file/svg/png}"; done

getter = urllib.URLopener()

EMOJIS_DIR = './emojis/'

if not os.path.isdir(EMOJIS_DIR):
    os.makedirs(EMOJIS_DIR)
    
print "Downloading base emoji:"

for i, emoji in enumerate(EMOJIS):
    filename = os.path.join(EMOJIS_DIR, "%03d.svg" % i)

    if os.path.isfile(filename):
        continue

    link = "https://tikolu.github.io/emojimix/emojis/" + "_".join(emoji[2]) + ".svg"
    print "--> (%03d/%03d): %s" % (i + 1, MAX_EMOJI_COUNT, EMOJIS[i][0])
    getter.retrieve(link, filename)

print "Downloading base emoji complete!"

extensionCode = "-ufe0f"

if not os.path.isdir(MERGED_DIR):    
    os.makedirs(MERGED_DIR)

print "Downloading merged emoji:"

for i in xrange(MAX_EMOJI_COUNT):
    for j in xrange(i, MAX_EMOJI_COUNT):
        filename = os.path.join(MERGED_DIR, "%03d_%03d.png" % (i, j))
        
        if os.path.isfile(filename):
            continue

        print "--> (%03d/%03d): [%s] x [%s]" % (i + 1, j + 1, EMOJIS[i][0], EMOJIS[j][0])
        
        code1 = "-".join(["u%s" % code for code in EMOJIS[i][2]])
        code2 = "-".join(["u%s" % code for code in EMOJIS[j][2]])
        links = []

        try: 
            for extensionCode in ["-ufe0f", ""]:
                code1e = code1 + (extensionCode if len(EMOJIS[i][2]) > 1 else "")
                code2e = code2 + (extensionCode if len(EMOJIS[j][2]) > 1 else "") 

                try:
                    pre = EMOJIS[i][1]
                    u1 = code1e
                    u2 = code2e
                    link = "https://www.gstatic.com/android/keyboard/emojikitchen/%s/%s/%s_%s.png" % (pre, u1, u1, u2)
                    links += [link]
                    getter.retrieve(link, filename)
                except:
                    pre = EMOJIS[j][1]
                    u1 = code2e
                    u2 = code1e
                    link = "https://www.gstatic.com/android/keyboard/emojikitchen/%s/%s/%s_%s.png" % (pre, u1, u1, u2)
                    links += [link]
                    getter.retrieve(link, filename)

                break
        except:
            for link in links:
                print "--> Failed: %s" % link

print "Downloading merged emoji complete!"
