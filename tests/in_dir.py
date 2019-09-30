#!/usr/bin/python3

import os
import glob
from tdr_py import vp_tide as vt

dirlist = glob.glob('*/')
for dir in dirlist:
	os.chdir(dir)

	merge = vt.v_merge('Asia/Jayapura')
	merge.to_csv('MERGE.TXT', sep='\t')

	os.chdir('..')

# os.chdir() #* insert path with single quotes
# os.listdir() #* directories & files in a list []