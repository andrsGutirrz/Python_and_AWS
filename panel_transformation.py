# creating an empty panel
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Create a df with known values
data = {
    'Item1' : pd.DataFrame({
        'a':[11,41],
        'b':[21,51],
        'c':[31,61],
    }),
    'Item2' : pd.DataFrame({
        'z':[12,42],
        'y':[22,52],
        'z':[32,62],
    }),
    'Item3' : pd.DataFrame({
        't':[13,43],
        'u':[23,53],
        'o':[33,63],
    }),
}

panel = pd.Panel(data)
print(panel)
pass