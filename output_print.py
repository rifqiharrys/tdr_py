#!/usr/bin/python3

import numpy as np
import pandas as pd 
import valeport_processing as vp 
import matplotlib.pyplot as plt

vsort = vp.valeport_sort()
x = vsort.index
y = vsort.Depth
# vsort.plot(x, y)

# output
# vsort.to_csv('SORT.TXT', sep='\t')

# plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Data Awal')
# plt.xlabel('Waktu')
# plt.ylabel('Kedalaman (m)')
# plt.legend(loc='best')
plt.show()