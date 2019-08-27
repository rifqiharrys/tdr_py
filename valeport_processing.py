#!/usr/bin/python3

import pandas as pd 
import glob 

def v_input(raw, tz = 'UTC', ntz = 'UTC'):
	data = pd.read_csv(raw, sep='\t', header=21, index_col='Timestamp') # Data reading, header cutting, line number 21 = column
	data = data.iloc[1:, 0:2] #null data @index 0 removed
	data.index = pd.to_datetime(data.index, dayfirst=True)
	data.index = data.index.tz_localize(tz)
	data.index = data.index.tz_convert(ntz)
	return data

def v_merge(tz = 'UTC', ntz = 'UTC'):
	txtlist = glob.glob('*.[Tt][Xx][Tt]')
	dummy = []

	for txt in txtlist:
		df = v_input(txt, tz, ntz)
		dummy.append(df)

	return pd.concat(dummy)

def v_sort(tz = 'UTC', ntz = 'UTC'):
	merged = v_merge(tz, ntz)
	return merged.sort_index()


#TODO: time adjusting, local & UTC