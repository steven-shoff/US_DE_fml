import matplotlib.pyplot as plt
import pandas as pd
import numpy as numpy

data = pd.read_csv('../data/acs2015_county_data.csv', encoding='latin-1')
print('data successfully loaded')
#print data