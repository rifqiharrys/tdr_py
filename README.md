# tdr_py
Tide Data Reform using python 3

valeport_processing.py is a module to process data acquired from Valeport depth recording instruments. It contains 3 functions:
-   v_input(raw, tz = 'UTC')
    Individual data reading
-   v_merge(tz = 'UTC')
    Multiple data merging and sorting
-   v_dirmerge(tz = 'UTC')
    Multiple data merging inside one tree level directory
