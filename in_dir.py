#!/usr/bin/python3

import os
import glob
import valeport_processing as vp

dirlist = glob.glob('*/')
for dir in dirlist:
	os.chdir(dir)

	os.chdir('..')

# os.chdir() #* insert path with single quotes
# os.listdir() #* directories & files in a list []