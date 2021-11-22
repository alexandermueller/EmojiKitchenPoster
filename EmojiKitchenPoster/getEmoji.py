#!/usr/bin/python

from lxml import html
import requests
import urllib
import os

getter = urllib.URLopener()
emojis = [       
        ("grinning face with smiling eyes", "20201001", "1f604", "https://tikolu.github.io/emojimix/emojis/1f604.svg"),
        ("grinning face", "20201001", "1f600", "https://tikolu.github.io/emojimix/emojis/1f600.svg"),
        ("slightly smiling face", "20201001", "1f642", "https://tikolu.github.io/emojimix/emojis/1f642.svg"),
        ("upside-down face", "20201001", "1f643", "https://tikolu.github.io/emojimix/emojis/1f643.svg"),
        ("winking face", "20201001", "1f609", "https://tikolu.github.io/emojimix/emojis/1f609.svg"),
        ("smiling face with smiling eyes", "20201001", "1f60a", "https://tikolu.github.io/emojimix/emojis/1f60a.svg"),
        ("grinning squinting face", "20201001", "1f606", "https://tikolu.github.io/emojimix/emojis/1f606.svg"),
        ("grinning face with big eyes", "20201001", "1f603", "https://tikolu.github.io/emojimix/emojis/1f603.svg"),
        ("beaming face with smiling eyes", "20201001", "1f601", "https://tikolu.github.io/emojimix/emojis/1f601.svg"),
        ("rolling on the floor laughing", "20201001", "1f923", "https://tikolu.github.io/emojimix/emojis/1f923.svg"),
        ("grinning face with sweat", "20201001", "1f605", "https://tikolu.github.io/emojimix/emojis/1f605.svg"),
        ("face with tears of joy", "20201001", "1f602", "https://tikolu.github.io/emojimix/emojis/1f602.svg"),
        ("smiling face with halo", "20201001", "1f607", "https://tikolu.github.io/emojimix/emojis/1f607.svg"),
        ("smiling face with hearts", "20201001", "1f970", "https://tikolu.github.io/emojimix/emojis/1f970.svg"),
        ("smiling face with heart-eyes", "20201001", "1f60d", "https://tikolu.github.io/emojimix/emojis/1f60d.svg"),
        ("face blowing a kiss", "20201001", "1f618", "https://tikolu.github.io/emojimix/emojis/1f618.svg"),
        ("star-struck", "20201001", "1f929", "https://tikolu.github.io/emojimix/emojis/1f929.svg"),
        ("kissing face", "20201001", "1f617", "https://tikolu.github.io/emojimix/emojis/1f617.svg"),
        ("kissing face with closed eyes", "20201001", "1f61a", "https://tikolu.github.io/emojimix/emojis/1f61a.svg"),
        ("kissing face with smiling eyes", "20201001", "1f619", "https://tikolu.github.io/emojimix/emojis/1f619.svg"),
        ("face with tongue", "20201001", "1f61b", "https://tikolu.github.io/emojimix/emojis/1f61b.svg"),
        ("squinting face with tongue", "20201001", "1f61d", "https://tikolu.github.io/emojimix/emojis/1f61d.svg"),
        ("face savoring food", "20201001", "1f60b", "https://tikolu.github.io/emojimix/emojis/1f60b.svg"),
        ("smiling face with tear", "20201001", "1f972", "https://tikolu.github.io/emojimix/emojis/1f972.svg"),
        ("money-mouth face", "20201001", "1f911", "https://tikolu.github.io/emojimix/emojis/1f911.svg"),
        ("winking face with tongue", "20201001", "1f61c", "https://tikolu.github.io/emojimix/emojis/1f61c.svg"),
        ("smiling face with open hands hugs", "20201001", "1f917", "https://tikolu.github.io/emojimix/emojis/1f917.svg"),
        ("shushing face quiet whisper", "20201001", "1f92b", "https://tikolu.github.io/emojimix/emojis/1f92b.svg"),
        ("thinking face question hmmm", "20201001", "1f914", "https://tikolu.github.io/emojimix/emojis/1f914.svg"),
        ("face with hand over mouth embarrassed", "20201001", "1f92d", "https://tikolu.github.io/emojimix/emojis/1f92d.svg"),
        ("face with raised eyebrow question", "20201001", "1f928", "https://tikolu.github.io/emojimix/emojis/1f928.svg"),
        ("zipper-mouth face", "20201001", "1f910", "https://tikolu.github.io/emojimix/emojis/1f910.svg"),
        ("neutral face", "20201001", "1f610", "https://tikolu.github.io/emojimix/emojis/1f610.svg"),
        ("expressionless face", "20201001", "1f611", "https://tikolu.github.io/emojimix/emojis/1f611.svg"),
        ("face without mouth", "20201001", "1f636", "https://tikolu.github.io/emojimix/emojis/1f636.svg"),
        ("zany face", "20201001", "1f92a", "https://tikolu.github.io/emojimix/emojis/1f92a.svg"),
        ("face in clouds", "20210218", "1f636-200d-1f32b", "https://tikolu.github.io/emojimix/emojis/1f636_200d_1f32b.svg"),
        ("smirking face suspicious", "20201001", "1f60f", "https://tikolu.github.io/emojimix/emojis/1f60f.svg"),
        ("unamused face", "20201001", "1f612", "https://tikolu.github.io/emojimix/emojis/1f612.svg"),
        ("face with rolling eyes", "20201001", "1f644", "https://tikolu.github.io/emojimix/emojis/1f644.svg"),
        ("grimacing face", "20201001", "1f62c", "https://tikolu.github.io/emojimix/emojis/1f62c.svg"),
        ("face exhaling", "20210218", "1f62e-200d-1f4a8", "https://tikolu.github.io/emojimix/emojis/1f62e_200d_1f4a8.svg"),
        ("lying face", "20201001", "1f925", "https://tikolu.github.io/emojimix/emojis/1f925.svg"),
        ("relieved face", "20201001", "1f60c", "https://tikolu.github.io/emojimix/emojis/1f60c.svg"),
        ("pensive face", "20201001", "1f614", "https://tikolu.github.io/emojimix/emojis/1f614.svg"),
        ("sleepy face", "20201001", "1f62a", "https://tikolu.github.io/emojimix/emojis/1f62a.svg"),
        ("drooling face", "20201001", "1f924", "https://tikolu.github.io/emojimix/emojis/1f924.svg"),
        ("sleeping face", "20201001", "1f634", "https://tikolu.github.io/emojimix/emojis/1f634.svg"),
        ("face with medical mask", "20201001", "1f637", "https://tikolu.github.io/emojimix/emojis/1f637.svg"),
        ("face with thermometer", "20201001", "1f912", "https://tikolu.github.io/emojimix/emojis/1f912.svg"),
        ("face with head-bandage", "20201001", "1f915", "https://tikolu.github.io/emojimix/emojis/1f915.svg"),
        ("nauseated face", "20201001", "1f922", "https://tikolu.github.io/emojimix/emojis/1f922.svg"),
        ("face vomiting throw", "20201001", "1f92e", "https://tikolu.github.io/emojimix/emojis/1f92e.svg"),
        ("sneezing face", "20201001", "1f927", "https://tikolu.github.io/emojimix/emojis/1f927.svg"),
        ("hot face warm", "20201001", "1f975", "https://tikolu.github.io/emojimix/emojis/1f975.svg"),
        ("cold face freezing ice", "20201001", "1f976", "https://tikolu.github.io/emojimix/emojis/1f976.svg"),
        ("face with crossed-out eyes", "20201001", "1f635", "https://tikolu.github.io/emojimix/emojis/1f635.svg"),
        ("woozy face drunk tipsy drug high", "20201001", "1f974", "https://tikolu.github.io/emojimix/emojis/1f974.svg"),
        ("exploding head mindblow", "20201001", "1f92f", "https://tikolu.github.io/emojimix/emojis/1f92f.svg"),
        ("cowboy hat face", "20201001", "1f920", "https://tikolu.github.io/emojimix/emojis/1f920.svg"),
        ("partying face", "20201001", "1f973", "https://tikolu.github.io/emojimix/emojis/1f973.svg"),
        ("disguised face", "20201001", "1f978", "https://tikolu.github.io/emojimix/emojis/1f978.svg"),
        ("face with monocle glasses", "20201001", "1f9d0", "https://tikolu.github.io/emojimix/emojis/1f9d0.svg"),
        ("smiling face with sunglasses", "20201001", "1f60e", "https://tikolu.github.io/emojimix/emojis/1f60e.svg"),
        ("confused face", "20201001", "1f615", "https://tikolu.github.io/emojimix/emojis/1f615.svg"),
        ("worried face", "20201001", "1f61f", "https://tikolu.github.io/emojimix/emojis/1f61f.svg"),
        ("slightly frowning face", "20201001", "1f641", "https://tikolu.github.io/emojimix/emojis/1f641.svg"),
        ("face with open mouth", "20201001", "1f62e", "https://tikolu.github.io/emojimix/emojis/1f62e.svg"),
        ("hushed face", "20201001", "1f62f", "https://tikolu.github.io/emojimix/emojis/1f62f.svg"),
        ("astonished face", "20201001", "1f632", "https://tikolu.github.io/emojimix/emojis/1f632.svg"),
        ("nerd face glasses", "20201001", "1f913", "https://tikolu.github.io/emojimix/emojis/1f913.svg"),
        ("flushed face", "20201001", "1f633", "https://tikolu.github.io/emojimix/emojis/1f633.svg"),
        ("pleading face", "20201001", "1f97a", "https://tikolu.github.io/emojimix/emojis/1f97a.svg"),
        ("anguished face", "20201001", "1f627", "https://tikolu.github.io/emojimix/emojis/1f627.svg"),
        ("fearful face", "20201001", "1f628", "https://tikolu.github.io/emojimix/emojis/1f628.svg"),
        ("frowning face with open mouth", "20201001", "1f626", "https://tikolu.github.io/emojimix/emojis/1f626.svg"),
        ("anxious face with sweat", "20201001", "1f630", "https://tikolu.github.io/emojimix/emojis/1f630.svg"),
        ("sad but relieved face", "20201001", "1f625", "https://tikolu.github.io/emojimix/emojis/1f625.svg"),
        ("loudly crying face", "20201001", "1f62d", "https://tikolu.github.io/emojimix/emojis/1f62d.svg"),
        ("weary face", "20201001", "1f629", "https://tikolu.github.io/emojimix/emojis/1f629.svg"),
        ("crying face", "20201001", "1f622", "https://tikolu.github.io/emojimix/emojis/1f622.svg"),
        ("persevering face", "20201001", "1f623", "https://tikolu.github.io/emojimix/emojis/1f623.svg"),
        ("angry face", "20201001", "1f620", "https://tikolu.github.io/emojimix/emojis/1f620.svg"),
        ("downcast face with sweat", "20201001", "1f613", "https://tikolu.github.io/emojimix/emojis/1f613.svg"),
        ("confounded face", "20201001", "1f616", "https://tikolu.github.io/emojimix/emojis/1f616.svg"),
        ("face with symbols on mouth", "20201001", "1f92c", "https://tikolu.github.io/emojimix/emojis/1f92c.svg"),
        ("disappointed face", "20201001", "1f61e", "https://tikolu.github.io/emojimix/emojis/1f61e.svg"),
        ("tired face", "20201001", "1f62b", "https://tikolu.github.io/emojimix/emojis/1f62b.svg"),
        ("face with steam from nose", "20201001", "1f624", "https://tikolu.github.io/emojimix/emojis/1f624.svg"),
        ("yawning face", "20201001", "1f971", "https://tikolu.github.io/emojimix/emojis/1f971.svg"),
        ("pile of poo", "20201001", "1f4a9", "https://tikolu.github.io/emojimix/emojis/1f4a9.svg"),
        ("pouting face", "20201001", "1f621", "https://tikolu.github.io/emojimix/emojis/1f621.svg"),
        ("face screaming in fear", "20201001", "1f631", "https://tikolu.github.io/emojimix/emojis/1f631.svg"),
        ("angry face with horns", "20201001", "1f47f", "https://tikolu.github.io/emojimix/emojis/1f47f.svg"),
        ("skull", "20201001", "1f480", "https://tikolu.github.io/emojimix/emojis/1f480.svg"),
        ("alien", "20201001", "1f47d", "https://tikolu.github.io/emojimix/emojis/1f47d.svg"),
        ("smiling face with horns devil", "20201001", "1f608", "https://tikolu.github.io/emojimix/emojis/1f608.svg"),
        ("clown face", "20201001", "1f921", "https://tikolu.github.io/emojimix/emojis/1f921.svg"),
        ("ghost", "20201001", "1f47b", "https://tikolu.github.io/emojimix/emojis/1f47b.svg"),
        ("robot", "20201001", "1f916", "https://tikolu.github.io/emojimix/emojis/1f916.svg"),
        ("hundred points percent", "20201001", "1f4af", "https://tikolu.github.io/emojimix/emojis/1f4af.svg"),
        ("eyes", "20201001", "1f440", "https://tikolu.github.io/emojimix/emojis/1f440.svg"),
        ("rose flower", "20201001", "1f339", "https://tikolu.github.io/emojimix/emojis/1f339.svg"),
        ("blossom flower", "20201001", "1f33c", "https://tikolu.github.io/emojimix/emojis/1f33c.svg"),
        ("tulip flower", "20201001", "1f337", "https://tikolu.github.io/emojimix/emojis/1f337.svg"),
        ("cactus", "20201001", "1f335", "https://tikolu.github.io/emojimix/emojis/1f335.svg"),
        ("pineapple", "20201001", "1f34d", "https://tikolu.github.io/emojimix/emojis/1f34d.svg"),
        ("birthday cake", "20201001", "1f382", "https://tikolu.github.io/emojimix/emojis/1f382.svg"),
        ("sunset", "20210831", "1f307", "https://tikolu.github.io/emojimix/emojis/1f307.svg"),
        ("cupcake muffin", "20201001", "1f9c1", "https://tikolu.github.io/emojimix/emojis/1f9c1.svg"),
        ("headphone earphone", "20210521", "1f3a7", "https://tikolu.github.io/emojimix/emojis/1f3a7.svg"),
        ("cherry blossom flower", "20210218", "1f338", "https://tikolu.github.io/emojimix/emojis/1f338.svg"),
        ("microbe germ bacteria virus covid corona", "20201001", "1f9a0", "https://tikolu.github.io/emojimix/emojis/1f9a0.svg"),
        ("bouquet flowers", "20201001", "1f490", "https://tikolu.github.io/emojimix/emojis/1f490.svg"),
        ("hot dog food", "20201001", "1f32d", "https://tikolu.github.io/emojimix/emojis/1f32d.svg"),
        ("kiss mark lips", "20201001", "1f48b", "https://tikolu.github.io/emojimix/emojis/1f48b.svg"),
        ("jack-o-lantern pumpkin", "20201001", "1f383", "https://tikolu.github.io/emojimix/emojis/1f383.svg"),
        ("cheese wedge", "20201001", "1f9c0", "https://tikolu.github.io/emojimix/emojis/1f9c0.svg"),
        ("hot beverage coffee cup tea", "20201001", "2615", "https://tikolu.github.io/emojimix/emojis/2615.svg"),
        ("confetti ball", "20201001", "1f38a", "https://tikolu.github.io/emojimix/emojis/1f38a.svg"),
        ("balloon", "20201001", "1f388", "https://tikolu.github.io/emojimix/emojis/1f388.svg"),
        ("snowman without snow", "20201001", "26c4", "https://tikolu.github.io/emojimix/emojis/26c4.svg"),
        ("gem stone crystal diamond", "20201001", "1f48e", "https://tikolu.github.io/emojimix/emojis/1f48e.svg"),
        ("evergreen tree", "20201001", "1f332", "https://tikolu.github.io/emojimix/emojis/1f332.svg"),
        ("lemon", "20210521", "1f34b", "https://tikolu.github.io/emojimix/emojis/1f34b.svg"),
        ("scorpion", "20210218", "1f982", "https://tikolu.github.io/emojimix/emojis/1f982.svg"),
        ("see-no-evil monkey", "20201001", "1f648", "https://tikolu.github.io/emojimix/emojis/1f648.svg"),
        ("broken heart", "20201001", "1f494", "https://tikolu.github.io/emojimix/emojis/1f494.svg"),
        ("love letter heart", "20201001", "1f48c", "https://tikolu.github.io/emojimix/emojis/1f48c.svg"),
        ("heart with arrow", "20201001", "1f498", "https://tikolu.github.io/emojimix/emojis/1f498.svg"),
        ("heart decoration", "20201001", "1f49f", "https://tikolu.github.io/emojimix/emojis/1f49f.svg"),
        ("revolving hearts", "20201001", "1f49e", "https://tikolu.github.io/emojimix/emojis/1f49e.svg"),
        ("beating heart", "20201001", "1f493", "https://tikolu.github.io/emojimix/emojis/1f493.svg"),
        ("two hearts", "20201001", "1f495", "https://tikolu.github.io/emojimix/emojis/1f495.svg"),
        ("growing heart", "20201001", "1f497", "https://tikolu.github.io/emojimix/emojis/1f497.svg"),
        ("orange heart", "20201001", "1f9e1", "https://tikolu.github.io/emojimix/emojis/1f9e1.svg"),
        ("yellow heart", "20201001", "1f49b", "https://tikolu.github.io/emojimix/emojis/1f49b.svg"),
        ("mending heart", "20210218", "2764-200d-1fa79", "https://tikolu.github.io/emojimix/emojis/2764_200d_1fa79.svg"),
        ("purple heart", "20201001", "1f49c", "https://tikolu.github.io/emojimix/emojis/1f49c.svg"),
        ("green heart", "20201001", "1f49a", "https://tikolu.github.io/emojimix/emojis/1f49a.svg"),
        ("blue heart", "20201001", "1f499", "https://tikolu.github.io/emojimix/emojis/1f499.svg"),
        ("brown heart", "20201001", "1f90e", "https://tikolu.github.io/emojimix/emojis/1f90e.svg"),
        ("white heart", "20201001", "1f90d", "https://tikolu.github.io/emojimix/emojis/1f90d.svg"),
        ("black heart", "20201001", "1f5a4", "https://tikolu.github.io/emojimix/emojis/1f5a4.svg"),
        ("sparkling heart", "20201001", "1f496", "https://tikolu.github.io/emojimix/emojis/1f496.svg"),
        ("heart with ribbon", "20201001", "1f49d", "https://tikolu.github.io/emojimix/emojis/1f49d.svg"),
        ("bread", "20210831", "1f35e", "https://tikolu.github.io/emojimix/emojis/1f35e.svg"),
        ("newspaper", "20201001", "1f4f0", "https://tikolu.github.io/emojimix/emojis/1f4f0.svg"),
        ("crystal ball", "20201001", "1f52e", "https://tikolu.github.io/emojimix/emojis/1f52e.svg"),
        ("crown", "20201001", "1f451", "https://tikolu.github.io/emojimix/emojis/1f451.svg"),
        ("pig face", "20201001", "1f437", "https://tikolu.github.io/emojimix/emojis/1f437.svg"),
        ("unicorn", "20210831", "1f984", "https://tikolu.github.io/emojimix/emojis/1f984.svg"),
        ("first quarter moon face", "20201001", "1f31b", "https://tikolu.github.io/emojimix/emojis/1f31b.svg"),
        ("deer", "20201001", "1f98c", "https://tikolu.github.io/emojimix/emojis/1f98c.svg"),
        ("magic wand", "20210521", "1fa84", "https://tikolu.github.io/emojimix/emojis/1fa84.svg"),
        ("dizzy", "20201001", "1f4ab", "https://tikolu.github.io/emojimix/emojis/1f4ab.svg"),
        ("meow cat face", "20201001", "1f431", "https://tikolu.github.io/emojimix/emojis/1f431.svg"),
        ("lion", "20201001", "1f981", "https://tikolu.github.io/emojimix/emojis/1f981.svg"),
        ("fire", "20201001", "1f525", "https://tikolu.github.io/emojimix/emojis/1f525.svg"),
        ("bird", "20210831", "1f426", "https://tikolu.github.io/emojimix/emojis/1f426.svg"),
        ("bat", "20201001", "1f987", "https://tikolu.github.io/emojimix/emojis/1f987.svg"),
        ("owl", "20210831", "1f989", "https://tikolu.github.io/emojimix/emojis/1f989.svg"),
        ("strawberry", "20210831", "1f353", "https://tikolu.github.io/emojimix/emojis/1f353.svg"),
        ("rainbow", "20201001", "1f308", "https://tikolu.github.io/emojimix/emojis/1f308.svg"),
        ("monkey face", "20201001", "1f435", "https://tikolu.github.io/emojimix/emojis/1f435.svg"),
        ("honeybee bumblebee wasp", "20201001", "1f41d", "https://tikolu.github.io/emojimix/emojis/1f41d.svg"),
        ("turtle", "20201001", "1f422", "https://tikolu.github.io/emojimix/emojis/1f422.svg"),
        ("octopus", "20201001", "1f419", "https://tikolu.github.io/emojimix/emojis/1f419.svg"),
        ("llama alpaca", "20201001", "1f999", "https://tikolu.github.io/emojimix/emojis/1f999.svg"),
        ("goat", "20210831", "1f410", "https://tikolu.github.io/emojimix/emojis/1f410.svg"),
        ("panda", "20201001", "1f43c", "https://tikolu.github.io/emojimix/emojis/1f43c.svg"),
        ("koala", "20201001", "1f428", "https://tikolu.github.io/emojimix/emojis/1f428.svg"),
        ("sloth", "20201001", "1f9a5", "https://tikolu.github.io/emojimix/emojis/1f9a5.svg"),
        ("bear", "20210831", "1f43b", "https://tikolu.github.io/emojimix/emojis/1f43b.svg"),
        ("rabbit face", "20201001", "1f430", "https://tikolu.github.io/emojimix/emojis/1f430.svg"),
        ("hedgehog", "20201001", "1f994", "https://tikolu.github.io/emojimix/emojis/1f994.svg"),
        ("snail", "20210218", "1f40c", "https://tikolu.github.io/emojimix/emojis/1f40c.svg"),
        ("mouse face rat", "20201001", "1f42d", "https://tikolu.github.io/emojimix/emojis/1f42d.svg"),
        ("fish", "20210831", "1f41f", "https://tikolu.github.io/emojimix/emojis/1f41f.svg"),
        ("globe showing Europe-Africa", "20201001", "1f30d", "https://tikolu.github.io/emojimix/emojis/1f30d.svg"),
        ("sun with face", "20201001", "1f31e", "https://tikolu.github.io/emojimix/emojis/1f31e.svg"),
        ("glowing star", "20201001", "1f31f", "https://tikolu.github.io/emojimix/emojis/1f31f.svg"),
        ("star", "20201001", "2b50", "https://tikolu.github.io/emojimix/emojis/2b50.svg"),
        ("last quarter moon face", "20201001", "1f31c", "https://tikolu.github.io/emojimix/emojis/1f31c.svg"),
        ("avocado", "20201001", "1f95", "https://tikolu.github.io/emojimix/emojis/1f951.svg")
]

api = "https://www.gstatic.com/android/keyboard/emojikitchen/"
emojiPath = './emojis/'

for i, emoji in enumerate(emojis):
    if not os.path.isdir(emojiPath):
        os.makedirs(emojiPath)

    fullfilename = os.path.join(emojiPath, str(i) + ".svg")
    getter.retrieve(emoji[3], fullfilename)

mergedEmojisPath = './merged'

for i, link in enumerate(f):
    if not os.path.isdir(merged):
        os.makedirs(merged)
    
    # fullfilename = os.path.join(merged, str(i) + ".svg")
    # getter.retrieve(link, fullfilename)