#!/usr/bin/python3

import numpy as np 
import pandas as pd 
import glob
from matplotlib import pyplot as plt 

def valeport_input(raw):
	data = pd.read_table(raw, header=21, index_col='Timestamp') # Data reading, header cutting, line number 21 = column
	data = data.iloc[1:, 0:2] #null data @index 0 removed
	data.index = pd.to_datetime(data.index, dayfirst=True)
	return data

def valeport_merge():
	txtlist = glob.glob('*.[Tt][Xx][Tt]')
	dummy = []

	for txt in txtlist:
		txt = valeport_input(txt)
		dummy.append(txt)

	return pd.concat(dummy)

def valeport_sort():
	merged = valeport_merge()
	return merged.sort_index()

out = valeport_sort()
print(out)

#TODO: check if the data really sorted or already sorted after merged
# data.index = pd.to_datetime(data.Timestamp, dayfirst=True)
# print(data)

# output
# data.to_csv('V000147_OUT.TXT', sep='\t')