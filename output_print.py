#!/usr/bin/python3

import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt 
import valeport_processing as vp 

out = vp.valeport_sort()
print(out)
# output
# data.to_csv('V000147_OUT.TXT', sep='\t')