#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
from Constants import *

mergedDirectory = os.fsencode(MERGED_DIR)

if not os.path.isdir(MERGED_DIR):
    os.makedirs(MERGED_DIR)

emojiSet = set()
emojiTextFile = open(EMOJIS_TXT, 'r')
lines = emojiTextFile.readlines()

for line in lines:
    components = line[:-1].split(',')
    
    if len(components) != 3:
        break

    emojiSet.add(components[1])

mergedSet = set()

mergedDirectoryContents = os.listdir(mergedDirectory)

for i, file in enumerate(mergedDirectoryContents):
    filename = os.fsdecode(file)
    
    if filename.endswith('.png'):
        for code in filename.replace('.png', '').split("_"):
            mergedSet.add(code)

print('Checking mergedSet - emojiSet:')

difference = mergedSet.difference(emojiSet)
print('\n'.join(difference) if len(difference) > 0 else '-> mergedSet <= emojiSet')

