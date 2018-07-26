# This is a first Python file.  I'd like to create a .ipynb file, but this will do.

# Now I'll add some code

import numpy as np
import pandas as pd

# the succeeding function generatens numerical months
def thing(integer):
    m = integer
    while True:
        m =m%12 + 1
        yield m
