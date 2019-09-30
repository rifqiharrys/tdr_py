#!/usr/bin/python3

import numpy as np
import pandas as pd 
import valeport_processing as vp 
import matplotlib.pyplot as plt

vmerge = vp.v_merge()
x = vmerge.index
y = vmerge.Depth
# vsort.plot(x, y)

# output
# vsort.to_csv('SORT.TXT', sep='\t')

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Data Pasang Surut')
plt.xlabel('Waktu')
plt.ylabel('Ketinggian Muka Air dari Sensor (m)')
plt.legend(loc='best')
plt.show()