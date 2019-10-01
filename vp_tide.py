#!/usr/bin/python3

import pandas as pd 
import glob 

#! NOTE 
#? Indonesia timezone (tz):
#? WIB:	'Asia/Jakarta'
#? WITA:	'Asia/Makassar'
#? WIT:	'Asia/Jayapura'
#* full tz list
#* https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

def v_input(raw, tz = 'UTC'):
	# Data reading, header cutting until line number 21, data under Timestamp become index
	data = pd.read_csv(raw, sep='\t', header=21, index_col='Timestamp')

	# Remove null @index 0
	data = data.iloc[1:, 0:2]

	# Change timestamp to datetime dtype
	data.index = pd.to_datetime(data.index, dayfirst=True)

	# Add tz to dataframe, default: 'UTC'
	data.index = data.index.tz_localize(tz)

	return data

def v_merge(tz = 'UTC', sorting = True):
	# .txt file list
	txtlist = glob.glob('*.[Tt][Xx][Tt]')

	# Preparing to make list
	dummy = []

	# Insert data from some .txt files using v_input and append into list
	for txt in txtlist:
		df = v_input(txt, tz)
		dummy.append(df)

	# Merge list of data into one unsorted dataframe
	merged = pd.concat(dummy, sort=sorting)
	
	# Sorted dataframe by index (i.e. Timestamp) as output
	return merged.sort_index()
