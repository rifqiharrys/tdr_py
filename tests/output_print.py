#!/usr/bin/python3

import numpy as np
import pandas as pd 
from tdr_py import vp_tide as vt
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
vmerge = vt.v_dirmerge('Asia/Jakarta')
x = vmerge.index
y = vmerge.Depth
print(vmerge)
print(vmerge.dtypes)
# vmerge.to_csv('MERGE.TXT', sep = '\t')
# vsort.plot(x, y)
# output
# vsort.to_csv('SORT.TXT', sep='\t')

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Data Pasang Surut')
plt.xlabel('Waktu')
plt.ylabel('Ketinggian Muka Air dari Sensor (m)')
plt.legend(loc='best')
plt.show()

#! FutureWarning: Using an implicitly registered datetime converter for a matplotlib plotting method. The converter was registered by pandas on import. Future versions of pandas will require you to explicitly register matplotlib converters.

#* To register the converters:
#* 	>>> from pandas.plotting import register_matplotlib_converters
#* 	>>> register_matplotlib_converters()
