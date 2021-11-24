#!/usr/bin/env python3

import os
import shutil
from Constants import *

mergedDirectory = os.fsencode(MERGED_DIR)

if not os.path.isdir(REMERGED_DIR):
    os.makedirs(REMERGED_DIR)

mergedDirectoryContents = os.listdir(mergedDirectory)
totalEmojis = len(mergedDirectoryContents)

print("Renaming Merged Files:")

for i, file in enumerate(mergedDirectoryContents):
     filename = os.fsdecode(file)

     if filename.endswith(".png"):
        first, second = list(map(lambda x: int(x), filename.replace(".png", "").split("_")))
        newFilename = "%s_+_%s.png" % (EMOJIS[first][0].replace(" ", '_'), EMOJIS[second][0].replace(" ", '_'))
        shutil.copy("%s/%s" % (MERGED_DIR, filename), "%s/%s" % (REMERGED_DIR, newFilename))
        print("--> Copying (%05d/%05d): %s" % (i, totalEmojis, newFilename))

print("Finished")
