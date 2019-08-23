#!/usr/bin/python3

import numpy as np 
import pandas as pd 
import glob
from matplotlib import pyplot as plt 

def valeport_data(raw):
	data = pd.read_csv(raw, sep='\t', header=21) # Data reading, header cutting, line number 21 = column
	data = data.iloc[1:, 0:2] #null data @index 0 removed
	data.index = pd.to_datetime(data.Timestamp, dayfirst=True)
	return data

txtlist = glob.glob('*.[Tt][Xx][Tt]')

for txt in txtlist:
	data_in = valeport_data(txt)

#TODO: change Timestamp object type into datetime
# data.index = pd.to_datetime(data.Timestamp, dayfirst=True)
# print(data)

# output
# data.to_csv('V000147_OUT.TXT', sep='\t')