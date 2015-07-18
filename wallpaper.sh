#!/bin/bash

#This script will run the python file that generates a wallpaper and then sets the wallpaper using feh
touch /tmp/wallpaper.ppm
python generate.py
feh --bg-scale /tmp/wallpaper.ppm
