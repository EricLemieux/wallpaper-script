#!/bin/python3.4

import random

def lerp(x1, x2, t):
	return ((1-t)*x1 + t*x2)

#This script will generate a wallpaper file so that it can be set later
BUFFER = ""

#Set some variable we are going to need
#These should be read in as an argument or something but whatever they work for now
WIDTH = 1920
HEIGHT = 1080

file = open("/tmp/wallpaper.ppm", "w")

BUFFER += "P3 "
s = str(str(WIDTH) + " " + str(HEIGHT) + " 255 ")
BUFFER += s

START = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
TOP_RIGHT = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

BOT_LEFT = [random.randint(1,255), random.randint(1,255), random.randint(1,255)]

for y in range(HEIGHT):
	for x in range(WIDTH):
		BUFFER += str(int((lerp(START[0], TOP_RIGHT[0], x/WIDTH)+lerp(START[0], BOT_LEFT[0],y/HEIGHT))/2))
		BUFFER += " "
		BUFFER += str(int((lerp(START[1], TOP_RIGHT[1], x/WIDTH)+lerp(START[1], BOT_LEFT[1],y/HEIGHT))/2))
		BUFFER += " "
		BUFFER += str(int((lerp(START[2], TOP_RIGHT[2], x/WIDTH)+lerp(START[1], BOT_LEFT[2],y/HEIGHT))/2))
		BUFFER += " \n"

file.write(BUFFER)		
file.close()
