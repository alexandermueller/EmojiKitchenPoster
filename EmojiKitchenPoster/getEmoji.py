#!/usr/bin/python

from lxml import html
import requests
import urllib
import os

getter = urllib.URLopener()
emojis = [       
    ("grinning face with smiling eyes", "20201001", ["1f604"]),
    ("grinning face", "20201001", ["1f600"]),
    ("slightly smiling face", "20201001", ["1f642"]),
    ("upside-down face", "20201001", ["1f643"]),
    ("winking face", "20201001", ["1f609"]),
    ("smiling face with smiling eyes", "20201001", ["1f60a"]),
    ("grinning squinting face", "20201001", ["1f606"]),
    ("grinning face with big eyes", "20201001", ["1f603"]),
    ("beaming face with smiling eyes", "20201001", ["1f601"]),
    ("rolling on the floor laughing", "20201001", ["1f923"]),
    ("grinning face with sweat", "20201001", ["1f605"]),
    ("face with tears of joy", "20201001", ["1f602"]),
    ("smiling face with halo", "20201001", ["1f607"]),
    ("smiling face with hearts", "20201001", ["1f970"]),
    ("smiling face with heart-eyes", "20201001", ["1f60d"]),
    ("face blowing a kiss", "20201001", ["1f618"]),
    ("star-struck", "20201001", ["1f929"]),
    ("kissing face", "20201001", ["1f617"]),
    ("kissing face with closed eyes", "20201001", ["1f61a"]),
    ("kissing face with smiling eyes", "20201001", ["1f619"]),
    ("face with tongue", "20201001", ["1f61b"]),
    ("squinting face with tongue", "20201001", ["1f61d"]),
    ("face savoring food", "20201001", ["1f60b"]),
    ("smiling face with tear", "20201001", ["1f972"]),
    ("money-mouth face", "20201001", ["1f911"]),
    ("winking face with tongue", "20201001", ["1f61c"]),
    ("smiling face with open hands hugs", "20201001", ["1f917"]),
    ("shushing face quiet whisper", "20201001", ["1f92b"]),
    ("thinking face question hmmm", "20201001", ["1f914"]),
    ("face with hand over mouth embarrassed", "20201001", ["1f92d"]),
    ("face with raised eyebrow question", "20201001", ["1f928"]),
    ("zipper-mouth face", "20201001", ["1f910"]),
    ("neutral face", "20201001", ["1f610"]),
    ("expressionless face", "20201001", ["1f611"]),
    ("face without mouth", "20201001", ["1f636"]),
    ("zany face", "20201001", ["1f92a"]),
    ("face in clouds", "20210218", ["1f636", "200d", "1f32b"]),
    ("smirking face suspicious", "20201001", ["1f60f"]),
    ("unamused face", "20201001", ["1f612"]),
    ("face with rolling eyes", "20201001", ["1f644"]),
    ("grimacing face", "20201001", ["1f62c"]),
    ("face exhaling", "20210218", ["1f62e", "200d", "1f4a8"]),
    ("lying face", "20201001", ["1f925"]),
    ("relieved face", "20201001", ["1f60c"]),
    ("pensive face", "20201001", ["1f614"]),
    ("sleepy face", "20201001", ["1f62a"]),
    ("drooling face", "20201001", ["1f924"]),
    ("sleeping face", "20201001", ["1f634"]),
    ("face with medical mask", "20201001", ["1f637"]),
    ("face with thermometer", "20201001", ["1f912"]),
    ("face with head-bandage", "20201001", ["1f915"]),
    ("nauseated face", "20201001", ["1f922"]),
    ("face vomiting throw", "20201001", ["1f92e"]),
    ("sneezing face", "20201001", ["1f927"]),
    ("hot face warm", "20201001", ["1f975"]),
    ("cold face freezing ice", "20201001", ["1f976"]),
    ("face with crossed-out eyes", "20201001", ["1f635"]),
    ("woozy face drunk tipsy drug high", "20201001", ["1f974"]),
    ("exploding head mindblow", "20201001", ["1f92f"]),
    ("cowboy hat face", "20201001", ["1f920"]),
    ("partying face", "20201001", ["1f973"]),
    ("disguised face", "20201001", ["1f978"]),
    ("face with monocle glasses", "20201001", ["1f9d0"]),
    ("smiling face with sunglasses", "20201001", ["1f60e"]),
    ("confused face", "20201001", ["1f615"]),
    ("worried face", "20201001", ["1f61f"]),
    ("slightly frowning face", "20201001", ["1f641"]),
    ("face with open mouth", "20201001", ["1f62e"]),
    ("hushed face", "20201001", ["1f62f"]),
    ("astonished face", "20201001", ["1f632"]),
    ("nerd face glasses", "20201001", ["1f913"]),
    ("flushed face", "20201001", ["1f633"]),
    ("pleading face", "20201001", ["1f97a"]),
    ("anguished face", "20201001", ["1f627"]),
    ("fearful face", "20201001", ["1f628"]),
    ("frowning face with open mouth", "20201001", ["1f626"]),
    ("anxious face with sweat", "20201001", ["1f630"]),
    ("sad but relieved face", "20201001", ["1f625"]),
    ("loudly crying face", "20201001", ["1f62d"]),
    ("weary face", "20201001", ["1f629"]),
    ("crying face", "20201001", ["1f622"]),
    ("persevering face", "20201001", ["1f623"]),
    ("angry face", "20201001", ["1f620"]),
    ("downcast face with sweat", "20201001", ["1f613"]),
    ("confounded face", "20201001", ["1f616"]),
    ("face with symbols on mouth", "20201001", ["1f92c"]),
    ("disappointed face", "20201001", ["1f61e"]),
    ("tired face", "20201001", ["1f62b"]),
    ("face with steam from nose", "20201001", ["1f624"]),
    ("yawning face", "20201001", ["1f971"]),
    ("pile of poo", "20201001", ["1f4a9"]),
    ("pouting face", "20201001", ["1f621"]),
    ("face screaming in fear", "20201001", ["1f631"]),
    ("angry face with horns", "20201001", ["1f47f"]),
    ("skull", "20201001", ["1f480"]),
    ("alien", "20201001", ["1f47d"]),
    ("smiling face with horns devil", "20201001", ["1f608"]),
    ("clown face", "20201001", ["1f921"]),
    ("ghost", "20201001", ["1f47b"]),
    ("robot", "20201001", ["1f916"]),
    ("hundred points percent", "20201001", ["1f4af"]),
    ("eyes", "20201001", ["1f440"]),
    ("rose flower", "20201001", ["1f339"]),
    ("blossom flower", "20201001", ["1f33c"]),
    ("tulip flower", "20201001", ["1f337"]),
    ("cactus", "20201001", ["1f335"]),
    ("pineapple", "20201001", ["1f34d"]),
    ("birthday cake", "20201001", ["1f382"]),
    ("sunset", "20210831", ["1f307"]),
    ("cupcake muffin", "20201001", ["1f9c1"]),
    ("headphone earphone", "20210521", ["1f3a7"]),
    ("cherry blossom flower", "20210218", ["1f338"]),
    ("microbe germ bacteria virus covid corona", "20201001", ["1f9a0"]),
    ("bouquet flowers", "20201001", ["1f490"]),
    ("hot dog food", "20201001", ["1f32d"]),
    ("kiss mark lips", "20201001", ["1f48b"]),
    ("jack-o-lantern pumpkin", "20201001", ["1f383"]),
    ("cheese wedge", "20201001", ["1f9c0"]),
    ("hot beverage coffee cup tea", "20201001", ["2615"]),
    ("confetti ball", "20201001", ["1f38a"]),
    ("balloon", "20201001", ["1f388"]),
    ("snowman without snow", "20201001", ["26c4"]),
    ("gem stone crystal diamond", "20201001", ["1f48e"]),
    ("evergreen tree", "20201001", ["1f332"]),
    ("lemon", "20210521", ["1f34b"]),
    ("scorpion", "20210218", ["1f982"]),
    ("see-no-evil monkey", "20201001", ["1f648"]),
    ("broken heart", "20201001", ["1f494"]),
    ("love letter heart", "20201001", ["1f48c"]),
    ("heart with arrow", "20201001", ["1f498"]),
    ("heart decoration", "20201001", ["1f49f"]),
    ("revolving hearts", "20201001", ["1f49e"]),
    ("beating heart", "20201001", ["1f493"]),
    ("two hearts", "20201001", ["1f495"]),
    ("growing heart", "20201001", ["1f497"]),
    ("orange heart", "20201001", ["1f9e1"]),
    ("yellow heart", "20201001", ["1f49b"]),
    ("mending heart", "20210218", ["2764", "200d", "1fa79"]),
    ("purple heart", "20201001", ["1f49c"]),
    ("green heart", "20201001", ["1f49a"]),
    ("blue heart", "20201001", ["1f499"]),
    ("brown heart", "20201001", ["1f90e"]),
    ("white heart", "20201001", ["1f90d"]),
    ("black heart", "20201001", ["1f5a4"]),
    ("sparkling heart", "20201001", ["1f496"]),
    ("heart with ribbon", "20201001", ["1f49d"]),
    ("bread", "20210831", ["1f35e"]),
    ("newspaper", "20201001", ["1f4f0"]),
    ("crystal ball", "20201001", ["1f52e"]),
    ("crown", "20201001", ["1f451"]),
    ("pig face", "20201001", ["1f437"]),
    ("unicorn", "20210831", ["1f984"]),
    ("first quarter moon face", "20201001", ["1f31b"]),
    ("deer", "20201001", ["1f98c"]),
    ("magic wand", "20210521", ["1fa84"]),
    ("dizzy", "20201001", ["1f4ab"]),
    ("meow cat face", "20201001", ["1f431"]),
    ("lion", "20201001", ["1f981"]),
    ("fire", "20201001", ["1f525"]),
    ("bird", "20210831", ["1f426"]),
    ("bat", "20201001", ["1f987"]),
    ("owl", "20210831", ["1f989"]),
    ("strawberry", "20210831", ["1f353"]),
    ("rainbow", "20201001", ["1f308"]),
    ("monkey face", "20201001", ["1f435"]),
    ("honeybee bumblebee wasp", "20201001", ["1f41d"]),
    ("turtle", "20201001", ["1f422"]),
    ("octopus", "20201001", ["1f419"]),
    ("llama alpaca", "20201001", ["1f999"]),
    ("goat", "20210831", ["1f410"]),
    ("panda", "20201001", ["1f43c"]),
    ("koala", "20201001", ["1f428"]),
    ("sloth", "20201001", ["1f9a5"]),
    ("bear", "20210831", ["1f43b"]),
    ("rabbit face", "20201001", ["1f430"]),
    ("hedgehog", "20201001", ["1f994"]),
    ("snail", "20210218", ["1f40c"]),
    ("mouse face rat", "20201001", ["1f42d"]),
    ("fish", "20210831", ["1f41f"]),
    ("globe showing Europe-Africa", "20201001", ["1f30d"]),
    ("sun with face", "20201001", ["1f31e"]),
    ("glowing star", "20201001", ["1f31f"]),
    ("star", "20201001", ["2b50"]),
    ("last quarter moon face", "20201001", ["1f31c"]),
    ("avocado", "20201001", ["1f951"])
]

emojiCount = len(emojis)
emojiPath = './emojis/'

if not os.path.isdir(emojiPath):
    os.makedirs(emojiPath)
    
print "Downloading base emoji:"

for i, emoji in enumerate(emojis):
    filename = os.path.join(emojiPath, str(i) + ".svg")

    if os.path.isfile(filename):
        continue

    link = "https://tikolu.github.io/emojimix/emojis/" + "_".join(emoji[2]) + ".svg"
    print "--> (%03d/%03d): %s" % (i + 1, emojiCount, emojis[i][0])
    getter.retrieve(link, filename)

print "Downloading base emoji complete!"

mergedEmojiPath = './merged'
extensionCode = "-ufe0f"

if not os.path.isdir(mergedEmojiPath):    
    os.makedirs(mergedEmojiPath)

print "Downloading merged emoji:"

for i in xrange(emojiCount):
    for j in xrange(i, emojiCount):
        filename = os.path.join(mergedEmojiPath, "%03d_%03d.png" % (i, j))
        
        if os.path.isfile(filename):
            continue

        print "--> (%03d/%03d): [%s] x [%s]" % (i + 1, j + 1, emojis[i][0], emojis[j][0])
        
        code1 = "-".join(["u%s" % code for code in emojis[i][2]])
        code2 = "-".join(["u%s" % code for code in emojis[j][2]])
        links = []

        try: 
            for extensionCode in ["-ufe0f", ""]:
                code1e = code1 + (extensionCode if len(emojis[i][2]) > 1 else "")
                code2e = code2 + (extensionCode if len(emojis[j][2]) > 1 else "") 

                try:
                    pre = emojis[i][1]
                    u1 = code1e
                    u2 = code2e
                    link = "https://www.gstatic.com/android/keyboard/emojikitchen/%s/%s/%s_%s.png" % (pre, u1, u1, u2)
                    links += [link]
                    getter.retrieve(link, filename)
                except:
                    pre = emojis[j][1]
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
