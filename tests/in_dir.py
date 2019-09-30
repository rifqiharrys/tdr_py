#!/usr/bin/python3

import os
import glob
import valeport_processing as vp

dirlist = glob.glob('*/')
for dir in dirlist:
	os.chdir(dir)

	merge = vp.v_merge('Asia/Jayapura')
	merge.to_csv('MERGE.TXT', sep='\t')

	os.chdir('..')

# os.chdir() #* insert path with single quotes
# os.listdir() #* directories & files in a list []