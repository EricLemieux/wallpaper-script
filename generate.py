#!/bin/python3.4

#This script will generate a wallpaper file so that it can be set later

#Set some variable we are going to need
#These should be read in as an argument or something but whatever they work for now
WIDTH = 1920
HEIGHT = 1080

file = open("/tmp/wallpaper.ppm", "w")

file.write("P3 ")
s = str(str(WIDTH) + " " + str(HEIGHT) + " 255 ")
file.write(s)

for y in range(HEIGHT):
	for x in range(WIDTH):
		file.write(str(int(x / WIDTH * 255)))
		file.write(" ")
		file.write(str(int(y /HEIGHT * 255)))
		file.write(" 0 \n")		

file.close()
