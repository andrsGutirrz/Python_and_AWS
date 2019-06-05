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
        'a':[12,42],
        'b':[22,52],
        'c':[32,62],
    }),
    'Item3' : pd.DataFrame({
        'a':[13,43],
        'b':[23,53],
        'c':[33,63],
    }),
}

panel = pd.Panel(data)
print(panel)
pass

