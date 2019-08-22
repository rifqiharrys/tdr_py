import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 

data = pd.read_csv('V000147.TXT', sep='\t', header=21) # Data reading, header cutting, line number 21 = column
data = data.iloc[1:, 0:2] #null data @index 0 removed
data.index = pd.to_datetime(data.Timestamp, dayfirst=True)

print(data)

# output
data.to_csv('V000147_OUT.TXT', sep='\t')