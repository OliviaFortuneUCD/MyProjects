import pandas as pd


Dublin= pd.read_csv('Property.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
#print(Dublin)
print(Dublin.head(14))
