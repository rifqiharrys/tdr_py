import numpy as np 
import pandas as pd 
from scipy import fftpack
from matplotlib import pyplot as plt 

data = pd.read_csv('V000147.TXT', sep='\t', header=21) #Data reading, header cutting, line number 21 = column
data = data.iloc[1:-4, 0:2] #null data @index 0 removed, remove data at the end of aquisition #!(4 last data)
data.Timestamp = pd.to_datetime(data.Timestamp, dayfirst=True)
data.index = data.Timestamp
print(data)