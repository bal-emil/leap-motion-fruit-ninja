{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Readme:\
\
\
Hi! Welcome to my Term Project: Leap Motion Fruit Ninja!\
    This page is for describing each mode and giving credits\
\
    All the art for the game was done by my friend Jonas Petkus\
    The run function was taken off the 15-112 website course notes\
    The main external modules used are 'Leap' and 'Pillow' (PIL)\
    This project runs in PYTHON 2.7!!!\
\
This project is a Fruit Ninja rip-off in python but with Leap Motion to control the cursor and to slice fruit with your finger on screen. There are separate modes that you can read more about below.\
\
    Classic:\
\
    This is your classic version of Fruit Ninja. Fruits come up and the waves of\
    fruit get progressively harder as you play. If you hit a bomb or lose 3 lives, game over\
    Note: In this mode you can press 't' to activate "Trace Mode" which draws a series\
    of lines between the player cursor and the other fruit that represent the shortest\
    and most optimal path to take from your current location to slice all the fruit.\
    It is good if you are having trouble or just like playing with cool looking lines\
    You may also press 'p' to pasue.\
\
    Zen:\
\
    This is the Zen Mode of Fruit Ninja, there are no lives, just try to cut as many fruit\
    as possible, however slicing bombs reduces from your score.\
    Trace mode also can be activated on this mode.\
\
    Training:\
\
    This mode calibrates your ability to play and complete levels into your "Skill rating"\
    such that you find a skill rating you are at for playing the mode so you can practice\
    on the levels that are at your skill cap. That being said, you must play a good amount\
    of rounds before a player stabalizes at their Skill rating (0-10). There are a lot of factors \
    that go into the calculation of your skill rating after each round, such as if you \
    completed the level, if you hit a bomb, the time it takes to slice all the fruit, amount\
    of fruit hit per round, etc. Since this mode aims to calibrate the players actual skill,\
    trace mode is not an option on this mode.\
\
    AI:\
\
    This mode shows a built AI playing Fruit Ninja. All the main data that the AI takes into\
    account when playing the game is shown on the top of the screen in the mode. The lines represent\
    The distances to the fruit, the green dot represents the target, the green line represents the\
    AI's path to the closest and most optimal fruit to it in order to play the game. All other info\
    is seen at the top of the screen. Instead of loading the back button like other modes, you must\
    press Escape to exit this mode.\
\
\
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
\
How to run the project:\
\
Put all images in the file in the same folder. To run the file, go into terminal (or console) and type \'93python\'94 followed by the path to the main project run file named \'93mainRunFile\'94 to play the game. Make sure this runs the game in Python 2.\
If the images cannot be found due to some error, go into the mainRunFile and change the paths to all the necessary images as needed matched with their name in the file, then the game will run as long as it is in the same folder. (Lines 45-65 in \'93mainRunFile.py\'94 with file = \'93path\'93, these are specific to my computer and otherwise don\'92t work unless it is the exact path so do change those appropriately, then the rest of the project should run perfectly!\
Additionally, install all necessary external modules as seen below:\
\
\
Needed External Libraries:\
- Leap Motion Python, this is included in the submitted file but you can also download and install this\
from the leap motion developer website and put the required files into the same folder, but the module \'93Leap.py\'94 should be in the same folder as all the other files and images.\
-Pillow (PIL) : you can instal this by using \'93pip install Pillow\'94 or \'93pop install PIL\'94 in the command line.\
\
\
Commands and shortcuts:\
See above in all the game mode descriptions for all the shortcuts and commands that you can use in each respective mode, as they are specific to each mode or only some modes. Instructions during gameplay on the screen are also shown.\
\
\
\
\
}