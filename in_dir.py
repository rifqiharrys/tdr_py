#!/usr/bin/python3

import os
import glob
dirlist = glob.glob('*/')
for dir in dirlist:
	os.chdir(dir)

	os.chdir('..')

# os.chdir() #* insert path with single quotes
# os.listdir() #* directories & files in a list []