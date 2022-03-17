import pandas as pd
import os

directory = 'data\CLEAN DATA'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    print(filename)
    # checking if it is a xls file
    if f.endswith(".xlsx"):
        out = f.split('.')[0]+'.csv'
        df = pd.read_excel(f) # if only the first sheet is needed.
        df.to_csv(out, index=False)