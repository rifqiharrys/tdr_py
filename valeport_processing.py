#!/usr/bin/python3

import pandas as pd 
import glob 

def valeport_input(raw):
	data = pd.read_csv(raw, sep='\t', header=21, index_col='Timestamp') # Data reading, header cutting, line number 21 = column
	data = data.iloc[1:, 0:2] #null data @index 0 removed
	data.index = pd.to_datetime(data.index, dayfirst=True)
	return data

def valeport_merge():
	txtlist = glob.glob('*.[Tt][Xx][Tt]')
	dummy = []

	for txt in txtlist:
		df = valeport_input(txt)
		dummy.append(df)

	return pd.concat(dummy)

def valeport_sort():
	merged = valeport_merge()
	return merged.sort_index()


#TODO: time adjusting, local & UTC