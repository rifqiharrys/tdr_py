#!/usr/bin/python3

import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt 
import valeport_processing as vp 

vmerge = vp.valeport_merge()
vsort = vp.valeport_sort()

# output
vmerge.to_csv('MERGE.TXT', sep='\t')
vsort.to_csv('SORT.TXT', sep='\t')